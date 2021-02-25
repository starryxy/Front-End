// multiple counts

table = new SimpleTable("baby-2010.csv");

count1 = 0;  // boy counter
count2 = 0;  // girl counter

for (row: table) {

  // count boy names ending with "y"
  if (row.getField("name").endsWith("y") &&
      row.getField("gender") == "boy") {
    count1 = count1 + 1;
  }

  // count girl names end with "y"
  if (row.getField("name").endsWith("y") &&
      row.getField("gender") == "girl") {
    count2 = count2 + 1;
  }

}

print("boy count:", count1);
print("girl count:", count2);



table = new SimpleTable("survey-2012.csv");

// modify all text to be lowercase letters
table.convertToLowerCase();

count1 = 0;
count2 = 0;
count3 = 0;

// Count sprite, dr pepper, coke soda, including diet soda
for (row: table) {

  if (row.getField("soda") == "sprite" ||
      row.getField("soda") == "diet sprite") {
    count1 = count1 + 1;
  }

  if (row.getField("soda") == "dr pepper" ||
      row.getField("soda") == "diet dr pepper") {
    count2 = count2 + 1;
  }

  if (row.getField("soda") == "coke" ||
      row.getField("soda") == "diet coke") {
    count3 = count3 + 1;
  }
}
print("sprite + diet count:", count1);
print("dr pepper + diet count:", count2);
print("coke + diet count:", count3);
