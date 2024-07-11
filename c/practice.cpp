#include <bits/stdc++.h>
using namespace std;
 

int main(){
   char select;
   double x;
   double y;
   double result;

   cout<<"****************CALCULATOR*******************\n";

   cout<<"Enter operation you wanna  perform(*,+,-,/): ";
   cin>>select;

   cout<<"Enter first number: ";
   cin>>x;

   cout<<"Enter second number: ";
   cin>>y;

   switch (select)
   {
   case '*':
   cout<<"Result is: "<<x*y<<endl;
      break;
   case '+':
   cout<<"Result is: "<<x+y<<endl;
   break;

   case '-':
   cout<<"Result is: "<<x-y<<endl;
   break;

   case '/':
   cout<<"Result is: "<<x/y<<endl;
   break;

   
   default:
   cout<<"Please select valid operator"<<endl;
      break;
   }

   cout<<"********************************************";

   
}
   



   



