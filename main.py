#include <stdio.h> 
#include <string.h> 
int main() { 
float expense[100]; 
char category[100][20]; 
int count = 0, choice; 
float total; 
while (1) { 
printf("\n1. Add Expense\n2. View Expenses\n3. Total Expense\n4. Exit\n"); 
printf("Enter choice: "); 
scanf("%d", &choice); 
if (choice == 1) { 
printf("Enter expense amount: "); 
scanf("%f", &expense[count]); 
printf("Enter category: "); 
scanf("%s", category[count]); 
count++; 
} 
else if (choice == 2) { 
if (count == 0) 
printf("No expenses recorded.\n"); 
else { 
for (int i = 0; i < count; i++) 
printf("%d. %s - %.2f\n", i+1, category[i], expense[i]); 
} 
} 
else if (choice == 3) { 
total = 0; 
for (int i = 0; i < count; i++) 
total += expense[i]; 
printf("Total Expense: %.2f\n", total); 
} 
else if (choice == 4) { 
break; 
} 
} 
return 0;
