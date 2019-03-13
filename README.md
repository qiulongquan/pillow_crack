### 利用 Python 中的 pillow 库完成对验证码的破解
- 实现的原理 重点
- 代码分析

```
AI 与向量空间图像识别
在这里我们使用向量空间搜索引擎来做字符识别，它具有很多优点：

不需要大量的训练迭代
不会训练过度
你可以随时加入／移除错误的数据查看效果
很容易理解和编写成代码
提供分级结果，你可以查看最接近的多个匹配
对于无法识别的东西只要加入到搜索引擎中，马上就能识别了。
当然它也有缺点，例如分类的速度比神经网络慢很多，它不能找到自己的方法解决问题等等。

关于向量空间搜索引擎的原理可以参考这篇文章：http://ondoc.logand.com/d/2697/pdf

Don't panic。向量空间搜索引擎名字听上去很高大上其实原理很简单。拿文章里的例子来说：

你有 3 篇文档，我们要怎么计算它们之间的相似度呢？2 篇文档所使用的相同的单词越多，那这两篇文章就越相似！但是这单词太多怎么办，就由我们来选择几个关键单词，选择的单词又被称作特征，每一个特征就好比空间中的一个维度（x，y，z 等），一组特征就是一个矢量，每一个文档我们都能得到这么一个矢量，只要计算矢量之间的夹角就能得到文章的相似度了。
```