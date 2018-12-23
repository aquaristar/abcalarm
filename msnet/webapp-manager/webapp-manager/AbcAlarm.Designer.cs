namespace webapp_manager
{
    partial class AbcAlarm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AbcAlarm));
            this.abcAlarmNotifyIcon = new System.Windows.Forms.NotifyIcon(this.components);
            this.contextMainMenuStrip = new System.Windows.Forms.ContextMenuStrip(this.components);
            this.viewAlarmsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem_StartAlarmServer = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuItem_Exit = new System.Windows.Forms.ToolStripMenuItem();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.contextMainMenuStrip.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.SuspendLayout();
            // 
            // abcAlarmNotifyIcon
            // 
            this.abcAlarmNotifyIcon.BalloonTipTitle = "ABC Warehouse";
            this.abcAlarmNotifyIcon.ContextMenuStrip = this.contextMainMenuStrip;
            this.abcAlarmNotifyIcon.Icon = ((System.Drawing.Icon)(resources.GetObject("abcAlarmNotifyIcon.Icon")));
            this.abcAlarmNotifyIcon.Text = "AbcAlarm Status";
            this.abcAlarmNotifyIcon.Visible = true;
            // 
            // contextMainMenuStrip
            // 
            this.contextMainMenuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.viewAlarmsToolStripMenuItem,
            this.toolStripMenuItem_StartAlarmServer,
            this.toolStripMenuItem_Exit});
            this.contextMainMenuStrip.Name = "contextMainMenuStrip";
            this.contextMainMenuStrip.Size = new System.Drawing.Size(140, 70);
            this.contextMainMenuStrip.Opening += new System.ComponentModel.CancelEventHandler(this.contextMainMenuStrip_Opening);
            // 
            // viewAlarmsToolStripMenuItem
            // 
            this.viewAlarmsToolStripMenuItem.Name = "viewAlarmsToolStripMenuItem";
            this.viewAlarmsToolStripMenuItem.Size = new System.Drawing.Size(139, 22);
            this.viewAlarmsToolStripMenuItem.Text = "View Alarms";
            this.viewAlarmsToolStripMenuItem.Click += new System.EventHandler(this.viewAlarmsToolStripMenuItem_Click);
            // 
            // toolStripMenuItem_StartAlarmServer
            // 
            this.toolStripMenuItem_StartAlarmServer.Name = "toolStripMenuItem_StartAlarmServer";
            this.toolStripMenuItem_StartAlarmServer.Size = new System.Drawing.Size(139, 22);
            this.toolStripMenuItem_StartAlarmServer.Text = "Stop";
            this.toolStripMenuItem_StartAlarmServer.Click += new System.EventHandler(this.toolStripMenuItem_StartAlarmServer_Click);
            // 
            // toolStripMenuItem_Exit
            // 
            this.toolStripMenuItem_Exit.Name = "toolStripMenuItem_Exit";
            this.toolStripMenuItem_Exit.Size = new System.Drawing.Size(139, 22);
            this.toolStripMenuItem_Exit.Text = "Exit";
            this.toolStripMenuItem_Exit.Click += new System.EventHandler(this.toolStripMenuItem_Exit_Click);
            // 
            // dataGridView1
            // 
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(-1, -2);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.Size = new System.Drawing.Size(910, 474);
            this.dataGridView1.TabIndex = 1;
            // 
            // AbcAlarm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(905, 473);
            this.Controls.Add(this.dataGridView1);
            this.Name = "AbcAlarm";
            this.Text = "AbcAlarm";
            this.WindowState = System.Windows.Forms.FormWindowState.Minimized;
            this.Load += new System.EventHandler(this.AbcAlarm_Load);
            this.contextMainMenuStrip.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.NotifyIcon abcAlarmNotifyIcon;
        private System.Windows.Forms.ContextMenuStrip contextMainMenuStrip;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem_StartAlarmServer;
        private System.Windows.Forms.ToolStripMenuItem toolStripMenuItem_Exit;
        private System.Windows.Forms.ToolStripMenuItem viewAlarmsToolStripMenuItem;
        private System.Windows.Forms.DataGridView dataGridView1;
    }
}

