#centos

##U盘安装
1.前置条件
	安装有windows操作系统的电脑一台
	能上网的环境
	大于4G的U盘
	centos7操作系统DVD安装包
	[win32diskimager](https://sourceforge.net/projects/win32diskimager/)
2.制作U盘驱动
	运行win32diskimager软件，找到你下载的centos安装文件(ISO格式)
	选择你的U盘
	点击写入并确定格式化
3.使用U盘安装
	把U盘插入要安装的电脑
	设置从U盘启动
	接下就是实际的centos安装了
4.备注
	无法使用UltraISO
	对于CentOS7，在Window上制作镜像的话，由于CentOS有一个特别的分区问题，所以有些Windows工具就不能正确的将U盘做成启动盘。目前为止不可以的工具有：unetbootin 和 universal usb installer。可以 的工具有Rufus, Fedora LiveUSB Creator,Win32 Disk Image, Rawrite32和dd。原文如下：
	the CentOS 7 installer image has a special partitioning which, as of July 2014, most Windows tools do NOT transfer correctly leading to undefined behaviour when booting from the USB key. Applications known (so far) to NOT work are unetbootin and "universal usb installler". Confirmed as functioning correctly are Rufus, Fedora LiveUSB Creator, Win32 Disk Imager, Rawrite32 and dd for Windows.