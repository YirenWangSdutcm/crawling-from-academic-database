# crawling-from-academic-database
simulate browser environment for automated literature retrieval
C:\Windows\System32>C:\Users\YeeRhenh（这里是你的admin地址）\AppData\Local\Programs\Python\Python313\python.exe -m pip install selenium

###### 安装命令：

python -m pip install --upgrade pip
pip install selenium
pip install webdriver-manager
pip install beautifulsoup4

###### 各种库的作用解释：

Selenium（自动化测试工具）模拟浏览器操作。目标网站使用JavaScript动态加载内容，普通HTTP请求（如requests库）无法获取渲染后的页面内容。Selenium驱动Chrome浏览器，执行点击、滚动、输入，获取完整页面源码。打开PubMed，输入关键词，提交搜索，跳转到摘要。

Webdriver-Manager（自动下载管理浏览器对应的驱动ChromeDriver）通过`ChromeDriverManager().install()`自动获取和配置正确的驱动路径。

BeautifulSoup4（解析HTML/XML）从Selenium获取的网页源码中定位标签属性元素，提取HTML结构化数据。（标题、作者、期刊等信息）解析文章列表和摘要。

###### 验证安装pip list | findstr "selenium webdriver-manager beautifulsoup4"

###### 输出结果（库版本号）

beautifulsoup4     4.12.3
selenium           4.19.0
webdriver-manager  4.0.1![image-20250411013022852](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411013022852.png)

![image-20250411013109837](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411013109837.png)

###### 代码阅读：开头导入多个库：selenium的相关模块、webdriver_manager的ChromeDriverManager、BeautifulSoup、以及time、json、os等标准库。selenium用于自动化浏览器操作，webdriver_manager自动管理浏览器驱动，BeautifulSoup解析HTML内容，time用于等待页面加载，json和os用于保存结果到桌面。![image-20250411013632000](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411013632000.png)

初始化WebDriver，使用ChromeDriverManager自动安装和配置Chrome驱动。定义关键词列表和结果容器。函数fetch_articles负责抓取每个关键词的文章数据。在函数内部，访问PubMed主页，定位搜索框，输入关键词，提交搜索。等待结果加载，用BeautifulSoup解析页面，提取文章的基本信息，跳转到摘要页面获取摘要内容，将数据存为字典，所有信息存入结果列表。![image-20250411013744963](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411013744963.png)主循环遍历关键词，调用fetch_articles函数，并打印处理进度。最后关闭浏览器，将结果保存为JSON文件到桌面。![image-20250411013822376](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411013822376.png)![image-20250411013902000](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411013902000.png)输出结果：![image-20250411013521162](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411013521162.png)保存的json文件：![image-20250411013600840](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411013600840.png)

将json文件转化为xlsx表格：下载pandas和openpyxl库：

pip install pandas

pip install openpyxl

![image-20250411015336537](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411015336537.png)

最终得到的xlsx文件数据：

![image-20250411015728767](C:\Users\YeeRhenh\AppData\Roaming\Typora\typora-user-images\image-20250411015728767.png)
