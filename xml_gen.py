import time

title = input("Title: ")
description = input("Description: ")
page_link = input("Page link (no https://): ")
date = time.strftime("%a, %e %b %Y %R PDT")
short_date = time.strftime("%b. %d, %Y")

print(f"""
    <item>
        <title>{title}</title>
        <description>{description}</description>
        <link>https://{page_link}</link>
        <guid>http://{page_link}</guid>
        <pubDate>{date}</pubDate>
    </item>

    <h2><i><a class="no-underscore" href="{page_link.split("/")[-1]}">{short_date} - {title}</a></i></h2>
    <p style ="margin-top: 0px; margin-bottom: 30px">{description}
    </p>
    <hr color="#303030">
""")