namespace client
{
    partial class FormClient
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
            this.textboxIncoming = new System.Windows.Forms.TextBox();
            this.textboxOutgoing = new System.Windows.Forms.TextBox();
            this.buttonSend = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // textboxIncoming
            // 
            this.textboxIncoming.Location = new System.Drawing.Point(12, 12);
            this.textboxIncoming.Multiline = true;
            this.textboxIncoming.Name = "textboxIncoming";
            this.textboxIncoming.ReadOnly = true;
            this.textboxIncoming.Size = new System.Drawing.Size(820, 490);
            this.textboxIncoming.TabIndex = 0;
            // 
            // textboxOutgoing
            // 
            this.textboxOutgoing.Location = new System.Drawing.Point(12, 508);
            this.textboxOutgoing.Multiline = true;
            this.textboxOutgoing.Name = "textboxOutgoing";
            this.textboxOutgoing.Size = new System.Drawing.Size(678, 81);
            this.textboxOutgoing.TabIndex = 1;
            // 
            // buttonSend
            // 
            this.buttonSend.Location = new System.Drawing.Point(696, 508);
            this.buttonSend.Name = "buttonSend";
            this.buttonSend.Size = new System.Drawing.Size(136, 81);
            this.buttonSend.TabIndex = 2;
            this.buttonSend.Text = "SEND";
            this.buttonSend.UseVisualStyleBackColor = true;
            this.buttonSend.Click += new System.EventHandler(this.buttonSend_Click);
            // 
            // FormClient
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(844, 602);
            this.Controls.Add(this.buttonSend);
            this.Controls.Add(this.textboxOutgoing);
            this.Controls.Add(this.textboxIncoming);
            this.Name = "FormClient";
            this.Text = "ChatApp Client";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textboxIncoming;
        private System.Windows.Forms.TextBox textboxOutgoing;
        private System.Windows.Forms.Button buttonSend;
    }
}