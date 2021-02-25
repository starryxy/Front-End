// count

table = new SimpleTable("baby-2010.csv");

count = 0;
// count num of rows with name starting with "A"
for (row: table) {
  if (row.getField("name").startsWith("A")) {
    print(row);
    count = count + 1;  // increases the value in count by 1
  }
}
// return the total count
print("count:", count);


count = 0;
// count num of rows with girl name starting with "A"
for (row: table) {
  if (row.getField("name").startsWith("A") &&
      row.getField("gender") == 'girl') {
    print(row);
    count = count + 1;  // increases the value in count by 1
  }
}
// return the total count
print("count:", count);
