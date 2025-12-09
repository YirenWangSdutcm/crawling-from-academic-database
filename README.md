(b站)crawling-from-academic-database

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
<img width="957" height="1046" alt="image" src="https://github.com/user-attachments/assets/561d28cc-e150-4321-91a4-9a4c03871986" />
<img width="944" height="477" alt="image" src="https://github.com/user-attachments/assets/a37b3305-910c-4245-af01-cd7c1262e81d" />

###### 代码阅读：开头导入多个库：selenium的相关模块、webdriver_manager的ChromeDriverManager、BeautifulSoup、以及time、json、os等标准库。selenium用于自动化浏览器操作，webdriver_manager自动管理浏览器驱动，BeautifulSoup解析HTML内容，time用于等待页面加载，json和os用于保存结果到桌面。

初始化WebDriver，使用ChromeDriverManager自动安装和配置Chrome驱动。定义关键词列表和结果容器。函数fetch_articles负责抓取每个关键词的文章数据。在函数内部，访问PubMed主页，定位搜索框，输入关键词，提交搜索。等待结果加载，用BeautifulSoup解析页面，提取文章的基本信息，跳转到摘要页面获取摘要内容，将数据存为字典，所有信息存入结果列表。

<img width="1910" height="897" alt="image" src="https://github.com/user-attachments/assets/8e4b575e-be8a-4194-9195-942823ccbbe7" />

主循环遍历关键词，调用fetch_articles函数，并打印处理进度。最后关闭浏览器，将结果保存为JSON文件到桌面。
<img width="1916" height="812" alt="image" src="https://github.com/user-attachments/assets/40d78585-c6ed-4478-9c5e-f25d0d635559" />
<img width="1919" height="318" alt="image" src="https://github.com/user-attachments/assets/acafe27b-c778-4272-8c50-3bdef7ad7bdd" />

输出结果：
<img width="1549" height="642" alt="image" src="https://github.com/user-attachments/assets/e34c49f9-99f0-4dfa-acfa-c611f96ae0d3" />

保存的json文件：
<img width="1242" height="704" alt="image" src="https://github.com/user-attachments/assets/8636bcc1-23af-470f-87ef-829a79e4a325" />

将json文件转化为xlsx表格：下载pandas和openpyxl库：

pip install pandas

pip install openpyxl

<img width="870" height="621" alt="image" src="https://github.com/user-attachments/assets/57e9e7bf-9a35-466c-8926-045560a55265" />


最终得到的xlsx文件数据：

<img width="416" height="183" alt="image" src="https://github.com/user-attachments/assets/a48e1f9d-846e-4764-9f63-138c5669e07b" />

