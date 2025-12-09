<img width="957" height="1046" alt="image" src="https://github.com/user-attachments/assets/a2aa02d6-edcb-4969-af97-2672f1b2cd9b" /># crawling-from-academic-database
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
webdriver-manager  4.0.1
<img width="957" height="1046" alt="图片 1" src="https://github.com/user-attachments/assets/e61da6af-7d43-4d8e-993a-b8c48654a4b8" />
<img width="944" height="477" alt="image" src="https://github.com/user-attachments/assets/ebe480e5-e7d0-410a-bb22-d3632f90a89d" />

###### 代码阅读：开头导入多个库：selenium的相关模块、webdriver_manager的ChromeDriverManager、BeautifulSoup、以及time、json、os等标准库。selenium用于自动化浏览器操作，webdriver_manager自动管理浏览器驱动，BeautifulSoup解析HTML内容，time用于等待页面加载，json和os用于保存结果到桌面。
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b806c7d5-61a8-4b08-87a5-5b2e5d07ebd5" />

初始化WebDriver，使用ChromeDriverManager自动安装和配置Chrome驱动。定义关键词列表和结果容器。函数fetch_articles负责抓取每个关键词的文章数据。在函数内部，访问PubMed主页，定位搜索框，输入关键词，提交搜索。等待结果加载，用BeautifulSoup解析页面，提取文章的基本信息，跳转到摘要页面获取摘要内容，将数据存为字典，所有信息存入结果列表。
<img width="1910" height="897" alt="image" src="https://github.com/user-attachments/assets/9edcceb2-9b24-442d-a3db-048c524c85aa" />

主循环遍历关键词，调用fetch_articles函数，并打印处理进度。最后关闭浏览器，将结果保存为JSON文件到桌面。
<img width="1916" height="812" alt="image" src="https://github.com/user-attachments/assets/747ef23c-b10d-4381-8bca-67d2552c2fae" />
<img width="1919" height="318" alt="image" src="https://github.com/user-attachments/assets/1daf8b28-16b8-4f18-b14d-cf7d60490211" />
输出结果：<img width="432" height="18" alt="image" src="https://github.com/user-attachments/assets/3f7d2deb-20b9-4baa-99fc-ca95821a1958" />
保存的json文件：<img width="432" height="18" alt="image" src="https://github.com/user-attachments/assets/7a9ab3c2-9e9b-4cc6-ab75-0c31031ce56a" />
<img width="1904" height="1080" alt="image" src="https://github.com/user-attachments/assets/9277a604-c9e8-4fa2-8ec3-d29ac44b0cf6" />

<img width="1549" height="642" alt="image" src="https://github.com/user-attachments/assets/78475814-714c-477a-88c1-a9909c4d4691" />

将json文件转化为xlsx表格：下载pandas和openpyxl库：

pip install pandas

pip install openpyxl

<img width="870" height="621" alt="image" src="https://github.com/user-attachments/assets/fb622636-6bb1-4573-825a-f22eb5e7f5dd" />


最终得到的xlsx文件数据：

