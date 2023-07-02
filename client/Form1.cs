using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;

namespace client
{
    public partial class FormConnect : Form
    {
        Thread th;
        public FormConnect()
        {
            InitializeComponent();
        }

        public void openClient(string ip, int port, string format)
        {
            Application.Run(new FormClient(ip, port, format));
        }

        private void buttonConnect_Click(object sender, EventArgs e)
        {
            string ip = textboxIP.Text;
            if (string.IsNullOrEmpty(ip) )
            {
                MessageBox.Show("IP address can not be empty!", "Empty IP Address", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
            else
            {
                string ip_pattern = @"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b";
                bool ip_valid = Regex.IsMatch(ip, ip_pattern);
                if (!ip_valid )
                {
                    MessageBox.Show($"The IP address you entered ('{ip}') is not a valid IP address!", "Invalid IP Address", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                else
                {
                    string port_str = textboxPORT.Text;
                    if (string.IsNullOrEmpty(port_str) ) {
                        MessageBox.Show("Port number can not be empty!", "Empty Port number", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                    }
                    else
                    {
                        string port_pattern = @"^(?:0|6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3})$";
                        bool port_valid = Regex.IsMatch(port_str, port_pattern);
                        if (!port_valid )
                        {
                            MessageBox.Show($"The port number you entered ('{port_str}') is not a valid port number!", "Invalid Port Number", MessageBoxButtons.OK, MessageBoxIcon.Error);
                        }
                        else
                        {
                            int port = Convert.ToInt32(port_str);
                            string format = textboxFORMAT.Text;
                            if (string.IsNullOrEmpty(format) )
                            {
                                MessageBox.Show("Format can not be empty!\nUse utf-8", "Empty Format", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                            }
                            else
                            {
                                this.Close();
                                th = new Thread(() => openClient(ip, port, format));
                                th.SetApartmentState(ApartmentState.STA);
                                th.Start();
                            }

                        }
                    }
                }
            }
        }
    }
}
