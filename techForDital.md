# 毕业设计主要技术细节

！！！

程序只涉及基本的算法，并不设计基本的判断细节，比如窗口是否打开等等。

## 需要的module

python-v:3.9.13-amd63

以及附属的pip，pip使用最新版安装

```powershell
pip install --upgrade pip
```

```powershell
pip install pywin32
```

## 获取屏幕

### 根据窗口的标题获取位置

将窗口的标题（标题中的所有字符都需要输入）传入的win32api中的`win32gui.FindWindow(None, WINDOW_TITLE)`中，函数返回的是窗口的句柄。代码如下：

```python
WINDOW_TITLE = '<title name>'
window = win32gui.FindWindow(None, WINDOW_TITLE)
```

然后我们使用`win32gui.SetForegroundWindow(window)`将选定的窗口设定置顶。之后我们使用`GetWindowRect()`获取窗口的大小，该函数返回的是一个元组。代码如下：

```python
win32gui.SetForegroundWindow(window)
pos = win32gui.GetWindowRect(window)
```

### 总是更新监视区域

可以做到，并且效果还是不错的，但是对性能的损耗非常大，刚开始还可以保持在30帧左右，但马上就变成了10几帧。并不建议实时更新，最好就是将窗固定在一个位置，不必实时监控窗口的位置。

实现方法：将获取窗口位置与保存图像分成两个函数，每次保存图像都重新获得以此窗口位置。

### win32api相应的问题

#### 设备上下文（DC）

由Windows提供，可以实现应用程序操作硬件设备，同时可以保证硬件设备与程序的无关性。当一个窗口创建之后，系统会自动创建对应系统的DC。但是对于DC的所有操作都要使用句柄来操作。

#### 句柄

句柄可以用来操作DC，是获取对象的一种方法，一种广义的指针。通过调用Windows api可以获得一个句柄，使用该句柄可以用来操作内核。同样的，句柄可以像指针那样悬空，但是毫无意义。

#### 保存bmp文件

bmp文件从设备管理器导入，使用`np.shape()`函数显示出来的形状为（width, height, 3）但是从buffer中直接导入第三维变成了4，使用cv读取之后也可以正常显示。



### 截取需要的窗口图像

#### 获取屏幕

使用`win32gui.GetDesktopWindow`获取整个屏幕的句柄，进而获取设备上下文DC`win32gui.GetWindowDC`，获取DC之后便可以从句柄创建DC，这里返回的句柄就是我们需要的源DC。在内存中分配句柄，创建指定设备兼容的内存设备上下文。代码如下：

```python
hwin = win32gui.GetDesktopWindow()
hwindc = win32gui.GetWindowDC(hwin)
srcdc = win32ui.CreateDCFromHandle(hwindc)
memdc = srcdc.CreateCompatibleDC()
```

#### 保存图像

在Windows中bmp文件非常通用，使用win32api可以直接对bmp进行操作。因此我们可以将从屏幕获取的图像保存为bmp格式，之后进行操作。

首先创建一个空的bmp文件。之后创建一个与指定设备兼容的bmp，使用bmp对象替换DC对象。从源设备（屏幕）向目标设备传输bmp位块也就是保存图像。代码如下：

```python
bmp = win32ui.CreateBitmap()
bmp.CreateCompatibleBitmap()
memdc.SelectObject(bmp)
memdc.Bitblt((0, 0), (width, height), srcdc, (left, up), win32con.SRCCOPY)
```

将指定位图的位图位复制到缓冲区，之后可以使用`numpy.frombuffer()`函数将缓冲区中的内容写入数组。从buffer中传入的数组是一个一维数组，可以使用np将其转换成对应的图像格式数组。代码如下：

```python
bufferArray = bmp.GetBitmapBits(True)
img = numpy.frombuffer(bufferArray, 'uint8')
```

最后我们要对DC以及句柄进行释放。原本存在的句柄要进行释放，自己创建的句柄要进行删除。代码如下：

```python
srcdc.DeleteDC()
memdc.DeleteDC()
win32gui.ReleaseDC(hwin, hwindc)
win32gui.DeleteObject(bmp.GetHandle())
```

### 屏幕缩放问题

在使用笔记本进行编写的时候发现很多时候无法对准需要监视的窗口。在调用win32api之后发现屏幕的分辨率之后原始分辨率缩放了125%，所以总是出现无法对准监视屏幕的问题。

<img src=".resources\\_photos\\test.bmp" alt="无法对齐监视窗口" style="zoom:50%;" />

使用win32api可以获取原始的分辨率与实际的分辨率，通过计算可以获得放大倍数，可以适应不同计算机的分辨率，以此来实时调整获取窗口的大小与位置。

### 获取连续的图像

使用while循环可以简单的获取到连续的图像，测试时使用`cv2.imshow()`函数测试，并做了benchmark可以达到平均30FPS ，在神经网络训练模型的时候足够使用。

循环的获取屏幕的尺寸会造成性能的急剧下降，把获取屏幕放大率移除出循环性能问题得以解决。帧率甚至能稳定在58帧左右，对于神经网络的训练完全足够。此问题彻底解决。