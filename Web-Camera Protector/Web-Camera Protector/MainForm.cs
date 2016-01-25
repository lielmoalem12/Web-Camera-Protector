using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net;
using System.Net.Sockets;

namespace Web_Camera_Protector
{
    public partial class MainForm : Form
    {
        #region ------  C O N S T -----------------
        private const string HOST = "127.0.0.1";
        private const int PORT = 5555;
        #endregion

        private NotifyIcon trayIcon;
        private ContextMenu trayMenu;
        Socket sockServer;

        public MainForm()
        {

            InitializeComponent();
            // Create a simple tray menu with only one item.
            trayMenu = new ContextMenu();
            trayMenu.MenuItems.Add("Open", OnOpen);
            trayMenu.MenuItems.Add("Exit", OnExit);
            // Create a tray icon. In this example we use a
            // standard system icon for simplicity, but youפ
            // can of course use your own custom icon too.
            trayIcon      = new NotifyIcon();
            trayIcon.Text = "MyTrayApp";
            trayIcon.Icon = Properties.Resources.old_cam_ra;
            trayIcon.MouseDoubleClick +=new MouseEventHandler(trayIcon_MouseDoubleClick);
 
            // Add menu to tray icon and show it.
            trayIcon.ContextMenu = trayMenu;
            trayIcon.Visible     = true;
            ConnectToServer();
        }

        #region --------   S E R V E R   S E S S I O N
        private void ConnectToServer()
        {
            this.sockServer = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            while (true)
            {
                try
                {
                    this.sockServer.Connect(HOST, PORT);
                    break;
                }
                catch (SocketException ex)  { continue; }
            }
        }

        public string Recive()
        {
            byte[] buffer = new byte[4096];
           
            try
            {
                int rec = this.sockServer.Receive(buffer);
                string msg = Encoding.UTF8.GetString(buffer).Substring(0, rec);
                return msg;
            }
            catch(SocketException ex)    { }
            return null;
        }

        public void Send(string message)
        {
            byte[] bytes = new byte[256];
            byte[] msg = Encoding.UTF8.GetBytes(message);
            try
            {
                int byteCount = this.sockServer.Send(msg, SocketFlags.None);
            }
            catch(SocketException ex)
            {
              //if (ex.ErrorCode == 10061)

            }
        }
        #endregion

        #region --------   E V E N T S
        protected override void OnLoad(EventArgs e)
        {
            Visible       = true; // Hide form window.
            ShowInTaskbar = true; // Remove from taskbar.
            trayIcon.Visible = false;
            StatusHandler();
            base.OnLoad(e);
        }

        protected void OnOpen(object sender, EventArgs e)
        {
            StatusHandler();
        }
 
        private void OnExit(object sender, EventArgs e)
        {
            trayIcon.Visible = false;
            Application.Exit();
        }
        
        public void trayIcon_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            this.ShowInTaskbar = true;
            trayIcon.Visible = false;
            StatusHandler();

        }

        private void MainForm_Resize(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {
                trayIcon.Visible = true;
                this.ShowInTaskbar = false;
                timerGetstatus.Enabled = false;
            }
        }      

        private void tabControl1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (tabControl1.SelectedIndex)
            {
                case 0:  // Status
                    StatusHandler();
                    break;
                case 1:  // WhiteList
                    WhiteListHandler();
                    break;
                case 2:  // BlackList
                    BlackListHandler();
                    break;

            }
        }

        private void KillButton_Click(object sender, EventArgs e)
        {
            Send("KillThis");
            StatusHandler();
        }

        private void timerGetstatus_Tick(object sender, EventArgs e)
        {
            StatusHandler();
        }


        #endregion

        private void BlackListHandler()
        {
            timerGetstatus.Enabled = false;
        }

        private void WhiteListHandler()
        {
            timerGetstatus.Enabled = false;
        }

        private void StatusHandler()
        {
                timerGetstatus.Enabled = true;
                Send( "Status");
                string Status = "";
                try
                {
                    Status = Recive();
                    string[] items = Status.Split('#');
                    Camera_Status.Text = items[0];
                    if (items[0] == "Camera is in use")
                    {
                        Process_Name.Text = items[1];
                        Size.Text = items[2];
                        Notes.Text = "None";
                    }
                    else 
                    {
                        Process_Name.Text = "None";
                        Size.Text = "None";
                        Notes.Text = "None";
                    }
                }
                catch
                {
                    Status = "Failed to connect";
                }
        }

    }
}
