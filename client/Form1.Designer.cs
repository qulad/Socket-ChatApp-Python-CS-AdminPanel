namespace client
{
    partial class FormConnect
    {
        /// <summary>
        ///Gerekli tasarımcı değişkeni.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///Kullanılan tüm kaynakları temizleyin.
        /// </summary>
        ///<param name="disposing">yönetilen kaynaklar dispose edilmeliyse doğru; aksi halde yanlış.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer üretilen kod

        /// <summary>
        /// Tasarımcı desteği için gerekli metot - bu metodun 
        ///içeriğini kod düzenleyici ile değiştirmeyin.
        /// </summary>
        private void InitializeComponent()
        {
            this.textboxIP = new System.Windows.Forms.MaskedTextBox();
            this.textboxPORT = new System.Windows.Forms.MaskedTextBox();
            this.labelIP = new System.Windows.Forms.Label();
            this.labelPORT = new System.Windows.Forms.Label();
            this.labelFORMAT = new System.Windows.Forms.Label();
            this.textboxFORMAT = new System.Windows.Forms.MaskedTextBox();
            this.buttonConnect = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // textboxIP
            // 
            this.textboxIP.Location = new System.Drawing.Point(169, 83);
            this.textboxIP.Name = "textboxIP";
            this.textboxIP.Size = new System.Drawing.Size(100, 22);
            this.textboxIP.TabIndex = 0;
            // 
            // textboxPORT
            // 
            this.textboxPORT.Location = new System.Drawing.Point(169, 150);
            this.textboxPORT.Name = "textboxPORT";
            this.textboxPORT.Size = new System.Drawing.Size(100, 22);
            this.textboxPORT.TabIndex = 1;
            this.textboxPORT.ValidatingType = typeof(int);
            // 
            // labelIP
            // 
            this.labelIP.AutoSize = true;
            this.labelIP.Location = new System.Drawing.Point(64, 86);
            this.labelIP.Name = "labelIP";
            this.labelIP.Size = new System.Drawing.Size(73, 16);
            this.labelIP.TabIndex = 2;
            this.labelIP.Text = "IP Address";
            // 
            // labelPORT
            // 
            this.labelPORT.AutoSize = true;
            this.labelPORT.Location = new System.Drawing.Point(64, 153);
            this.labelPORT.Name = "labelPORT";
            this.labelPORT.Size = new System.Drawing.Size(82, 16);
            this.labelPORT.TabIndex = 3;
            this.labelPORT.Text = "Port Number";
            // 
            // labelFORMAT
            // 
            this.labelFORMAT.AutoSize = true;
            this.labelFORMAT.Location = new System.Drawing.Point(64, 218);
            this.labelFORMAT.Name = "labelFORMAT";
            this.labelFORMAT.Size = new System.Drawing.Size(49, 16);
            this.labelFORMAT.TabIndex = 5;
            this.labelFORMAT.Text = "Format";
            // 
            // textboxFORMAT
            // 
            this.textboxFORMAT.Location = new System.Drawing.Point(169, 215);
            this.textboxFORMAT.Name = "textboxFORMAT";
            this.textboxFORMAT.Size = new System.Drawing.Size(100, 22);
            this.textboxFORMAT.TabIndex = 4;
            // 
            // buttonConnect
            // 
            this.buttonConnect.Location = new System.Drawing.Point(67, 287);
            this.buttonConnect.Name = "buttonConnect";
            this.buttonConnect.Size = new System.Drawing.Size(202, 23);
            this.buttonConnect.TabIndex = 6;
            this.buttonConnect.Text = "CONNECT";
            this.buttonConnect.UseVisualStyleBackColor = true;
            this.buttonConnect.Click += new System.EventHandler(this.buttonConnect_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(37, 23);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(257, 16);
            this.label1.TabIndex = 7;
            this.label1.Text = "CONNECT TO TCP/IP SOCKET SERVER";
            // 
            // FormConnect
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(324, 354);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.buttonConnect);
            this.Controls.Add(this.labelFORMAT);
            this.Controls.Add(this.textboxFORMAT);
            this.Controls.Add(this.labelPORT);
            this.Controls.Add(this.labelIP);
            this.Controls.Add(this.textboxPORT);
            this.Controls.Add(this.textboxIP);
            this.Name = "FormConnect";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Connect";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MaskedTextBox textboxIP;
        private System.Windows.Forms.MaskedTextBox textboxPORT;
        private System.Windows.Forms.Label labelIP;
        private System.Windows.Forms.Label labelPORT;
        private System.Windows.Forms.Label labelFORMAT;
        private System.Windows.Forms.MaskedTextBox textboxFORMAT;
        private System.Windows.Forms.Button buttonConnect;
        private System.Windows.Forms.Label label1;
    }
}

