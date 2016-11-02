#include <thread>
#include <windows.h>

bool running;
unsigned long StartTime;
unsigned int WaitTime = 5000;
const char* PrintString;
std::thread InternThread;

void MyPrint()
{
	while (running)
	{
		auto WaitedTime = GetTickCount() - StartTime;
		if (WaitedTime > WaitTime)
		{
			printf("Finished %s\n",PrintString);
			break;
		}
		Sleep(10);
	}
}


void TimeoutFunction(const char* MyString)
{
	printf("Startet %s\n", MyString);
	StartTime = GetTickCount();
	PrintString = MyString;
	running = false;
	if (InternThread.joinable())
	{
		InternThread.join();
	}

	running = true;
	InternThread = std::thread(MyPrint);
}


void TimeoutFunction2(const char* MyString)
{
	running = true;
	printf("Startet %s\n", MyString);
	StartTime = GetTickCount();
	PrintString = MyString;
	
	printf("%s is joinable %i\n", MyString, InternThread.joinable());
	if (!InternThread.joinable())
	{
		InternThread = std::thread(MyPrint);
	}
}

int main()
{
	TimeoutFunction2("A");
	Sleep(4000);
	TimeoutFunction2("B");
	Sleep(6000);
	TimeoutFunction2("C");
	Sleep(10000);
	TimeoutFunction2("D");
	Sleep(2000);
	TimeoutFunction2("E");
	TimeoutFunction2("F");
	TimeoutFunction2("G");

	InternThread.join();
	system("pause");
	return 0;
}