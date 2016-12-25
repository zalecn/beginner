#sqlite
[sqlite](http://system.data.sqlite.org/index.html/doc/trunk/www/downloads.wiki)
[sqlitebrowser](http://sqlitebrowser.org/)

#打印
##虚拟打印机
1. 没有打印管理
	将C:\Windows\system32\printmanagement.msc的快捷方式添加到管理工具文件夹中
2. 没有Microsoft XPS Document Writer
	控制面板->管理工具->打印管理
	依次点击“打印服务器”→（本地计算机）→驱动程序（找到Microsoft XOS Document Writer,如果没有需要自行下载，一般都是有的）→右键点击“打印机”，选择“添加打印机”
	选择“使用现有端口添加打印机”，也可以添加新端口，点击下一步。
	选择“使用计算机现有的打印机驱动程序”，找到“Microsoft XOS Document Writer”并点击，然后进行下一步。
	给打印机命名，然后点击下一步。
	进行安装前的最后检查，确认无误后点击下一步。
	等待片刻后，弹出完成对话框，点击完成。

 
> 操作步骤：
1、新建winform项目及创建窗体
2、拖取 打印 相关控件
   PageSetupDialog 、 PrintDialog 、 PrintDocument 、PrintPreviewDialog
3、设置上述控件的Document属性为相应的PrintDocument
4、设置按钮等控件 及 添加相应按钮事件

示意代码如下

	public partial class Form3 : Form  
	{  
	    public Form3()  
	    {  
	        InitializeComponent();  
	        this.printDocument1.OriginAtMargins = true;//启用页边距  
	        this.pageSetupDialog1.EnableMetric = true; //以毫米为单位  
	  
	    }  
	  
	    //打印设置  
	    private void btnSetPrint_Click(object sender, EventArgs e)  
	    {  
	        this.pageSetupDialog1.ShowDialog();   
	    }  
	  
	    //打印预览  
	    private void btnPrePrint_Click(object sender, EventArgs e)  
	    {  
	        this.printPreviewDialog1.ShowDialog();   
	    }  
	  
	    //打印  
	    private void btnPrint_Click(object sender, EventArgs e)  
	    {  
	        if (this.printDialog1.ShowDialog() == DialogResult.OK)  
	        {  
	            this.printDocument1.Print();  
	        }  
	    }  
	  
	    //打印内容的设置  
	    private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)  
	    {                          
	        ////打印内容 为 整个Form  
	        //Image myFormImage;  
	        //myFormImage = new Bitmap(this.Width, this.Height);  
	        //Graphics g = Graphics.FromImage(myFormImage);  
	        //g.CopyFromScreen(this.Location.X, this.Location.Y, 0, 0, this.Size);  
	        //e.Graphics.DrawImage(myFormImage, 0, 0);  
	  
	        ////打印内容 为 局部的 this.groupBox1  
	        //Bitmap _NewBitmap = new Bitmap(groupBox1.Width, groupBox1.Height);  
	        //groupBox1.DrawToBitmap(_NewBitmap, new Rectangle(0, 0, _NewBitmap.Width, _NewBitmap.Height));  
	        //e.Graphics.DrawImage(_NewBitmap, 0, 0, _NewBitmap.Width, _NewBitmap.Height);   
	  
	        //打印内容 为 自定义文本内容   
	        Font font = new Font("宋体", 12);  
	        Brush bru = Brushes.Blue;   
	        for (int i = 1; i <= 5; i++)  
	        {  
	            e.Graphics.DrawString("Hello world ", font, bru, i*20, i*20);  
	        }  
	    }  
	}  
 
