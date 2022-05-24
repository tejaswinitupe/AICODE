#include<iostream>
#include<conio.h>
#include<string.h>
#include<process.h>
//#include<studio.h>
using namespace std;
int main()
{
	char input[128];
	while(1)
	{
		gets(input);
		if(strcmp(input, "hi")==0){
			cout<<"hello";
		}
		if(strcmp(input, "hoe are you")==0){
			cout<<"i am fine";
		}
		
	}
}
