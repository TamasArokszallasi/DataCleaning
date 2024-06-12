# DataCleaning

The goal of this project was to create an automatic data cleaning in an excel file, which can not be done neither manually nor by the VBA.

The problem was the following:

There exist an excel file where there is only one column which contain cells below each other which all contains data structured exactly the same like this.

|subject|
|-------|
|Example name <br>type <br>country: UK  <br>Name: Big Dean <br>XiD: 1234 <br>XLiD: 4321 <br> E-mail: BigD@trialmail.com <br> UserID: BigD66 |

Well, i wanted to have each of these data in separate column like this:

|Name|Type|Country|Name|XiD|XLiD|E-mail|UserID|
|---|---|---|---|---|---|---|---|
|Example name|Type| UK| Big Dean| 1234| 4321| BigD@trialmail.com | BigD66|
