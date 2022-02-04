# map-reduce-mamidala-US_DisasterDeclarations

Link: [Data set reference](https://www.kaggle.com/headsortails/us-natural-disaster-declarations)

## Regarding Data:
The data I have used consist of natural disasters experienced in the different states of United States

From the initial dataset, I have mapped to the key-values: State, count. Then, I have used the terminal "sort" to get them sorted if they are not sorted. Then, I have reduced all the key values obtained after sorting and obtained the output and the combo graph is used to show the count of disasters occured in different states of US.

## powershell command
```
cat us_disaster_declarations.csv | python mam01mapper.py | sort | python mamreducer.py > sathya-output.txt

```

## Summary
**I wanted to find out which state has the highest number of disasters?** </br>
According to the report, the highest number of disasters occured in Texas,United States </br>

![NumberOfDisastersOccuredInDifferentStates](/images/NumberOfDisastersOccuredInDifferentStates.PNG)
