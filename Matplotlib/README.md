
### [Matplotlib教程](https://matplotlib.org/tutorials/index.html)
##### 相关链接
* Matplotlib 中文用户指南 3.5 艺术家教程：https://www.jianshu.com/p/aeb1cdf269ea
* Matplotlib 中文用户指南 3.1 pyplot教程：https://www.jianshu.com/p/c495e663f0ed?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation
-------
Matplotlib是一个Python 2D绘图库，可以在各种平台上以各种硬拷贝格式和交互式环境生成出版质量数据。Matplotlib可用于Python脚本，Python和IPythonshell，jupyter笔记本，Web应用程序服务器和四个图形用户界面工具包。／一个2D绘图库，可产生出版物质量的图表 
* 最基本的x-y函数图象:`plt.plot()`
以`y=sin(x),x=2πt；where t:[0,2]`的图象为例
示例代码：
 
``` t=np.arange(0.0,2.0,0.01)#自变量t
    s=np.sin(2*np.pi*t)#计算y
    #####必须语句######
    plt.plot(t,s)#指定x,y

    plt.xlabel('t')#x轴标签
    plt.ylabel('y')#y轴标签
    plt.title(r'image')#图象标题
    plt.grid(True)#画网格
    #####必须语句######
    plt.show()#画出图象
```
![三角函数曲线](http://7xrvee.com1.z0.glb.clouddn.com/17-10-7/25142090.jpg)

* 直方图:`plt.hist()`
画直方图最核心的函数为`plt.hist()`

    其主要参数有：
    * `x`:每个矩形条的高度,`list`等数组
    * `bins`:矩形条个数,`matplotlib`把矩形条称为“箱”

    返回值：
    *  n:矩形条高度（y轴）
    * bins:矩形条横向位置（x轴）
    * patches:矩形条对象，包含n,bins信息


以均值mu=100,方差sigma=15的正态分布的函数图像为例

```import matplotlib.mlab as mlab
    mu=100
    sigma=15
    x=mu+sigma*np.random.randn(10000)#生成矩形条高度

    num_bins=10#矩形条个数
    #####必须语句######
    n,bins,patches=plt.hist(x,num_bins)#传入矩形条高度和个数
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('histogram')
    #####必须语句######
    plt.show()
```
![直方图](http://7xrvee.com1.z0.glb.clouddn.com/17-10-7/24807033.jpg)

示例代码2

```import matplotlib.mlab as mlab
mu=100
sigma=15
x=mu+sigma*np.random.randn(10000)

num_bins=50

#normed=1表示画的是概率密度，和为1；facecolor：矩形条颜色；alpha：色深参数n,bins,patches=plt.hist(x,num_bins,normed=1,facecolor='green',alpha=0.5)
###画出一条逼近的曲线
y=mlab.normpdf(bins,mu,sigma)
plt.plot(bins,y,'r--')

plt.xlabel('x')
plt.ylabel('y')
plt.title('histogram')
plt.show()
```

![直方图](http://7xrvee.com1.z0.glb.clouddn.com/17-10-7/86941669.jpg)

* 3d离散点ax.scatter()

```
from mpl_toolkits.mplot3d import Axes3D
#x_list为离散点的list，内层list为一个三元组，每一个三元组代表三维空间中的一个点
x_list=[[1,2,3]]
fig=plt.figure()
ax=fig.gca(projection='3d')#返回坐标轴,projection还可以传入'polar'
for x in x_list:#遍历每个点，绘制
    ax.scatter(x[0],x[1],x[2],c='r')
plt.show()
```
![3d离散点](http://7xrvee.com1.z0.glb.clouddn.com/17-10-7/39844707.jpg)


* 3d空间曲面ax.plot_surface()

```from matplotlib import cm
from matplotlib.ticker import LinearLocator,FormatStrFormatter

fig=plt.figure()
ax=fig.gca(projection='3d')
X=np.arange(-5,5,0.1)#x坐标
Y=np.arange(-5,5,0.1)#y坐标
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)#计算出z坐标
#画表面:x,y,z坐标，rstride:横向步长，cstride:纵向步长，cmap:颜色，linewidth:线宽，antialiased:是否渐变
surf=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)

ax.set_zlim(-1.01,1.01)#坐标系的下边界和上边界
ax.zaxis.set_major_locator(LinearLocator(10))#设置Z轴标度
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))#Z轴精度
#shrink颜色条伸缩比例（0-1），aspect颜色条宽度（反比例，数值越大宽度越窄）
fig.colorbar(surf,shrink=0.5,aspect=5)

plt.show()
```
![3d空间曲面](http://7xrvee.com1.z0.glb.clouddn.com/17-10-7/96360206.jpg)

* 饼形图plt.pie()

```labels='Frogs','Hogs','Dogs','Logs'#设置标签
size=[15,30,45,10]#占比，和为100
colors=['yellow','gold','lightskyblue','lightcoral']#颜色
#展开第二个扇形，即Hogs，间距为0.1.注意explode传入的是一个tuple，哪个位置不为0，哪个对应的标签被展开，且不为0的数值就是展开的间距值
explode=(0,0.1,0,0)

#startangle控制饼状图的旋转方向
plt.pie(size,explode=explode,labels=labels,colors=colors,shadow=True,startangle=90)
plt.show()
```
![](http://7xrvee.com1.z0.glb.clouddn.com/17-10-7/15450298.jpg)


```labels='Frogs','Hogs','Dogs','Logs'
size=[15,30,45,10]
colors=['yellow','gold','lightskyblue','lightcoral']
explode=(0,0,0.1,0)#展开Dogs，间距值0.1

#autopct参数表示显示百分比，且决定了百分比的格式
plt.pie(size,explode=explode,labels=labels,colors=colors,shadow=True,autopct='%1.1f%%',startangle=90)
plt.show()
```

![](http://7xrvee.com1.z0.glb.clouddn.com/17-10-7/14370331.jpg)
