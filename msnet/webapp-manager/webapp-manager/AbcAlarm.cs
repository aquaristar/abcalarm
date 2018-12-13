using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
using Microsoft.Win32;

namespace webapp_manager
{
    public partial class AbcAlarm : Form
    {        
        private Process webapp;
        private string cPath = "webapp";
        private string cParams = "runserver 0.0.0.0:7000";
        private string processName = "ABCWarehouse Alarm";

        public AbcAlarm()
        {
            InitializeComponent();
        }
        
        private void AbcAlarm_Load(object sender, EventArgs e)
        {
            Console.WriteLine("=========== Load ABCWarehouse Alarm Server Controller ===========");            

            foreach (var process in Process.GetProcessesByName(processName))
            {
                process.Kill();
            }

            startProcess();
        }
        
        private void contextMainMenuStrip_Opening(object sender, CancelEventArgs e)
        {
            Console.WriteLine("opened");
        }

        private void toolStripMenuItem_StartAlarmServer_Click(object sender, EventArgs e)
        {           
            
            bool isRunning = Process.GetProcessesByName(processName)
                .FirstOrDefault() != default(Process); //p => p.MainModule.FileName.StartsWith(@"webapp")

            Console.WriteLine(isRunning.ToString());
            
            if (isRunning)
            {
                stopProcess();
            }
            else
            {
                startProcess();
            }            
        }

        private void toolStripMenuItem_Exit_Click(object sender, EventArgs e)
        {
            stopProcess();
            Console.WriteLine("exited");
            System.Windows.Forms.Application.Exit();
        }

        public void startProcess()
        {
            ProcessStartInfo startInfo = new ProcessStartInfo(string.Concat(processName, ".exe")); //cPath, "\\", 
            startInfo.Arguments = cParams;
            startInfo.UseShellExecute = false;
            startInfo.CreateNoWindow = true;
            webapp = System.Diagnostics.Process.Start(startInfo);

            toolStripMenuItem_StartAlarmServer.Text = "Stop";
            abcAlarmNotifyIcon.Icon = new System.Drawing.Icon(Path.GetFullPath(@"image\started.ico"));
        }

        public void stopProcess()
        {
            //webapp.CloseMainWindow();
            //webapp.Close();

            foreach (var process in Process.GetProcessesByName(processName))
            {
                process.Kill();
            }

            toolStripMenuItem_StartAlarmServer.Text = "Start";
            abcAlarmNotifyIcon.Icon = new System.Drawing.Icon(Path.GetFullPath(@"image\disabled.ico"));
        }

        private void viewAlarmsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Process.Start("http://localhost:7000/abcalarm/");
        }

        //private void SetStartup()
        //{
        //    RegistryKey rk = Registry.CurrentUser.OpenSubKey
        //        ("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", true);

        //    if (chkStartUp.Checked)
        //        rk.SetValue(AppName, Application.ExecutablePath);
        //    else
        //        rk.DeleteValue(AppName, false);

        //}
    }
}
