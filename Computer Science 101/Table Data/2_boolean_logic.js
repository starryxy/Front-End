// boolean logic

table = new SimpleTable("baby-2010.csv");

// print rows with name starting with "A" and ending with "y"
for (row: table) {
  if (row.getField("name").startsWith("A") &&
      row.getField("name").endsWith("y")) {
    print(row);
  }
}


// print rows with name starting with "X" or "Y" or "Z"
for (row: table) {
  if (row.getField("name").startsWith("X") ||
      row.getField("name").startsWith("Y") ||
      row.getField("name").startsWith("Z")) {
    print(row);
  }
}
