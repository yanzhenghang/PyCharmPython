import requests
from lxml import html
def main():
    payload = {
        "username": "&lt;2017140028&gt;",
        "password": "&lt;12146670&gt;",
        "lt": "&lt;LT-694385-aNbw653A771f1v5CRY3CX2ZIcppkOl-1520169607377&gt;"
    }
    header = { 'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}
    session_requests = requests.session()
    login_url = 'http://yjxt.bupt.edu.cn'
    result = session_requests.get(login_url)
    #print(result.text)
    tree = html.fromstring(result.text)
    #print(tree)
    authenticity_token = list(set(tree.xpath("//input[@name='lt']/@value")))[0]
    result = session_requests.post(login_url, data=payload, headers=header) #dict(referer=login_url)
    print(result.text)
    url0 = 'http://yjxt.bupt.edu.cn/Gstudent/Default.aspx?UID=2017140028'
    url = 'http://yjxt.bupt.edu.cn/Gstudent/Course/PlanCourseOnlineSel.aspx?EID=9kWb0OKGTBF2KzmBt5QNDZLXYu1Fldi6xwxV6Yb1wPA1TrsnKBRXgg==&UID=2017140028'
    #kv = {'user-agent': 'Mozilla/5.0'}
    print(dict(referer=url))
    result = session_requests.get(
        url0,
        headers=header
    )

    result = session_requests.get(
        url,
        headers=header
    )#.encoding = "utf-8"
    #dict(referer=url)
    #session_requests
    #    tree = html.fromstring(result.content)
    #bucket_elems = tree.findall(".//span[@class='repo-name']/")
    #bucket_names = [bucket.text_content.replace("n", "").strip() for bucket in bucket_elems]
    print(result.text)
    #print(result.text)

    return
main()