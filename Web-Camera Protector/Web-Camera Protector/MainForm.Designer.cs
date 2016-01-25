namespace Web_Camera_Protector
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                // Release the icon resource.
                trayIcon.Dispose();
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.tabControl1 = new System.Windows.Forms.TabControl();
            this.Status = new System.Windows.Forms.TabPage();
            this.KillButton = new System.Windows.Forms.Button();
            this.Notes = new System.Windows.Forms.Label();
            this.Size = new System.Windows.Forms.Label();
            this.Process_Name = new System.Windows.Forms.Label();
            this.Camera_Status = new System.Windows.Forms.Label();
            this.WhiteList = new System.Windows.Forms.TabPage();
            this.BlackList = new System.Windows.Forms.TabPage();
            this.timerGetstatus = new System.Windows.Forms.Timer(this.components);
            this.tabControl1.SuspendLayout();
            this.Status.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(3, 3);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(77, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Camera status:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(3, 84);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(38, 13);
            this.label2.TabIndex = 1;
            this.label2.Text = "Notes:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(3, 60);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(71, 13);
            this.label4.TabIndex = 3;
            this.label4.Text = "Process Size:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(3, 32);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(77, 13);
            this.label5.TabIndex = 4;
            this.label5.Text = "Process name:";
            // 
            // tabControl1
            // 
            this.tabControl1.Controls.Add(this.Status);
            this.tabControl1.Controls.Add(this.WhiteList);
            this.tabControl1.Controls.Add(this.BlackList);
            this.tabControl1.Location = new System.Drawing.Point(1, 0);
            this.tabControl1.Name = "tabControl1";
            this.tabControl1.SelectedIndex = 0;
            this.tabControl1.Size = new System.Drawing.Size(695, 337);
            this.tabControl1.TabIndex = 8;
            this.tabControl1.SelectedIndexChanged += new System.EventHandler(this.tabControl1_SelectedIndexChanged);
            // 
            // Status
            // 
            this.Status.Controls.Add(this.KillButton);
            this.Status.Controls.Add(this.Notes);
            this.Status.Controls.Add(this.Size);
            this.Status.Controls.Add(this.Process_Name);
            this.Status.Controls.Add(this.Camera_Status);
            this.Status.Controls.Add(this.label1);
            this.Status.Controls.Add(this.label2);
            this.Status.Controls.Add(this.label5);
            this.Status.Controls.Add(this.label4);
            this.Status.Location = new System.Drawing.Point(4, 22);
            this.Status.Name = "Status";
            this.Status.Padding = new System.Windows.Forms.Padding(3);
            this.Status.Size = new System.Drawing.Size(687, 311);
            this.Status.TabIndex = 0;
            this.Status.Text = "Status";
            this.Status.UseVisualStyleBackColor = true;
            // 
            // KillButton
            // 
            this.KillButton.Location = new System.Drawing.Point(76, 240);
            this.KillButton.Name = "KillButton";
            this.KillButton.Size = new System.Drawing.Size(75, 23);
            this.KillButton.TabIndex = 10;
            this.KillButton.Text = "Kill Process";
            this.KillButton.UseVisualStyleBackColor = true;
            this.KillButton.Click += new System.EventHandler(this.KillButton_Click);
            // 
            // Notes
            // 
            this.Notes.AutoSize = true;
            this.Notes.Location = new System.Drawing.Point(47, 84);
            this.Notes.Name = "Notes";
            this.Notes.Size = new System.Drawing.Size(0, 13);
            this.Notes.TabIndex = 9;
            // 
            // Size
            // 
            this.Size.AutoSize = true;
            this.Size.Location = new System.Drawing.Point(100, 60);
            this.Size.Name = "Size";
            this.Size.Size = new System.Drawing.Size(0, 13);
            this.Size.TabIndex = 7;
            // 
            // Process_Name
            // 
            this.Process_Name.AutoSize = true;
            this.Process_Name.Location = new System.Drawing.Point(100, 32);
            this.Process_Name.Name = "Process_Name";
            this.Process_Name.Size = new System.Drawing.Size(0, 13);
            this.Process_Name.TabIndex = 6;
            // 
            // Camera_Status
            // 
            this.Camera_Status.AutoSize = true;
            this.Camera_Status.Location = new System.Drawing.Point(100, 3);
            this.Camera_Status.Name = "Camera_Status";
            this.Camera_Status.Size = new System.Drawing.Size(0, 13);
            this.Camera_Status.TabIndex = 5;
            // 
            // WhiteList
            // 
            this.WhiteList.Location = new System.Drawing.Point(4, 22);
            this.WhiteList.Name = "WhiteList";
            this.WhiteList.Padding = new System.Windows.Forms.Padding(3);
            this.WhiteList.Size = new System.Drawing.Size(687, 311);
            this.WhiteList.TabIndex = 1;
            this.WhiteList.Text = "WhiteList";
            this.WhiteList.UseVisualStyleBackColor = true;
            // 
            // BlackList
            // 
            this.BlackList.Location = new System.Drawing.Point(4, 22);
            this.BlackList.Name = "BlackList";
            this.BlackList.Padding = new System.Windows.Forms.Padding(3);
            this.BlackList.Size = new System.Drawing.Size(687, 311);
            this.BlackList.TabIndex = 2;
            this.BlackList.Text = "BlackList";
            this.BlackList.UseVisualStyleBackColor = true;
            // 
            // timerGetstatus
            // 
            this.timerGetstatus.Interval = 1000;
            this.timerGetstatus.Tick += new System.EventHandler(this.timerGetstatus_Tick);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(690, 333);
            this.Controls.Add(this.tabControl1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "MainForm";
            this.Text = "Web Camera protector";
            this.Resize += new System.EventHandler(this.MainForm_Resize);
            this.tabControl1.ResumeLayout(false);
            this.Status.ResumeLayout(false);
            this.Status.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TabControl tabControl1;
        private System.Windows.Forms.TabPage Status;
        private System.Windows.Forms.Label Notes;
        private System.Windows.Forms.Label Size;
        private System.Windows.Forms.Label Process_Name;
        private System.Windows.Forms.Label Camera_Status;
        private System.Windows.Forms.TabPage WhiteList;
        private System.Windows.Forms.TabPage BlackList;
        private System.Windows.Forms.Button KillButton;
        private System.Windows.Forms.Timer timerGetstatus;
    }
}

