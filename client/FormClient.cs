using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace client
{
    public partial class FormClient : Form
    {
        private string ip;
        private int port;
        private string format;
        private NetworkStream stream;
        private TcpClient client;
        private CancellationTokenSource cancellationTokenSource;

        public FormClient(string ip, int port, string format)
        {
            this.ip = ip;
            this.port = port;
            this.format = format;
            InitializeComponent();
            this.FormClosing += new FormClosingEventHandler(Disconnect);
            Control.CheckForIllegalCrossThreadCalls = false;
            Connect();
            textboxOutgoing.Focus();
        }

        public void Connect()
        {
            this.client = new TcpClient();
            try
            {
                client.Connect(IPAddress.Parse(ip), port);
                this.stream = client.GetStream();
                cancellationTokenSource = new CancellationTokenSource();
                Thread receive = new Thread(ReceiveThread);
                receive.Start();
            }
            catch (ArgumentNullException e)
            {
                Console.WriteLine(e.Message);
                MessageBox.Show($"ArgumentNullException: {e}\nPlease close and re-open app!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (SocketException e)
            {
                MessageBox.Show($"SocketException: {e}\nPlease close and re-open app!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        public void Disconnect(object sender, FormClosingEventArgs e)
        {
            cancellationTokenSource.Cancel();
            this.client.Close();
        }

        public void Send(string message)
        {
            byte[] message_bytes= Encoding.UTF8.GetBytes(message);
            int message_length = message_bytes.Length;
            byte[] message_length_bytes = Encoding.UTF8.GetBytes(message_length.ToString());
            message_length_bytes = message_length_bytes.Concat(Encoding.UTF8.GetBytes(new string(' ', 64 - message_length_bytes.Length))).ToArray();
            this.stream.Write(message_length_bytes, 0, message_length_bytes.Length);
            this.stream.Write(message_bytes, 0, message_bytes.Length);
        }

        public void ReceiveThread()
        {
            while (!this.cancellationTokenSource.Token.IsCancellationRequested)
            {
                if (this.stream.DataAvailable)
                {
                    byte[] message_byte = new byte[2048];
                    this.stream.Read(message_byte, 0, message_byte.Length);
                    string message = Encoding.UTF8.GetString(message_byte);
                    textboxIncoming.Text += $"\r\n{message}";
                    //UpdateTextboxIncoming(message);
                }
                else
                {
                    Thread.Sleep(100);
                }
            }
        }

        private void UpdateTextboxIncoming(string message)
        {
            if (textboxIncoming.InvokeRequired)
            {
                textboxIncoming.Invoke((MethodInvoker)(() =>
                {
                    textboxIncoming.Text += $"\n{message}";
                }));
            }
            else
            {
                textboxIncoming.Text += $"\n{message}";
            }
        }

        private void buttonSend_Click(object sender, EventArgs e)
        {
            string text = textboxOutgoing.Text;
            Send(text);
            textboxOutgoing.Text = "";
        }
    }
}
