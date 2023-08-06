text_template = "Hello {:<10.10s} to my website {}! Your lucky number is: {:5.0f}"

name = "Anna"
website = "www.mywebsite.com"
lucky_number = 100 / 3


print(text_template.format(name, website, lucky_number))
