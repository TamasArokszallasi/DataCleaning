# DataCleaning

The goal of this project was to create an automatic data cleaning in an excel file, which can not be done neither manually nor by the VBA. **The exact variable names were modified in the public code to avoid any kind of fraud.**

The problem was the following:

There exist an excel file where there is only one column which contain cells below each other which all contains data structured exactly the same like this.

|subject|
|-------|
|Example name <br>type <br>country: UK  <br>Name: Big Dean <br>XiD: 1234 <br>XLiD: 4321 <br> E-mail: BigD@trialmail.com <br> UserID: BigD66 |

Well, i wanted to have each of these data in separate column like this:

|Type|Country|Name|XiD|E-mail|
|---|---|---|---|---|
|Type| UK| Big Dean| 1234| BigD@trialmail.com |

How would you do it in Excel? we can not find a proper way to it, so i turned to python and did the following:

I looked for the data between Name and Type, Country and Type and so, and the data i get from that i put that into a table, and then created an excel file which sorts all below each in the proper columns.
Now it's time for you to check the code.
Unfortunately, this project ended like this, mainly  beacuse it was not necessary to use python for this task. Furthermore, i was not having more time to develope further.

What sort of problems do i face with the code, which if this would continue i would definitely fix it!

-The biggest issue was the data insolvency, the fact that sometimes those cells rows were mixed, so in that case this code don't work, i had to fix it manually and later asked everyone to use a common template
-Capital letters, spaces and other disturbing things. The code was too sensitive and simple, if someone just not following the template, the code fully stops working and messing up everything.
-if 1 cell is wrong, almost all after it also gets wrong output in the excel. This should be the number one thing to resolve if.. If there is issue with the cell, the code should neglect it, or just highlight where does it occour and go further properly, not messing up everything.

-It could be a pretty interesting to work with, but i think maybe by VBA this task could also be solved, but since i was and am learning python, i choosed to do with it.

Thank you for reading it :)
