// Field names for the baby table: name, rank, gender, year
table = new SimpleTable("baby-2010.csv");

// print all rows with rank value 6
for (row: table) {
  if (row.getField("rank") == 6) {
    print(row);
  }
}


// startsWith, endsWith

// print rows with name starting with "Ab"
for (row: table) {
  if (row.getField("name").startsWith("Ab")) {
    print(row);
  }
}

// print rows with name ending with "z"
for (row: table) {
  if (row.getField("name").endsWith("z")) {
    print(row);
  }
}
