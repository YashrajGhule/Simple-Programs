// Need to link with Iphlpapi.lib and Ws2_32.lib
#define UNICODE
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iphlpapi.h>///
#include<Psapi.h>
#include <stdio.h>
#include<iostream>

#pragma comment(lib, "iphlpapi.lib")
#pragma comment(lib, "ws2_32.lib")

#define MALLOC(x) HeapAlloc(GetProcessHeap(), 0, (x))
#define FREE(x) HeapFree(GetProcessHeap(), 0, (x))

/* Note: could also use malloc() and free() */

int main()
{
    PMIB_TCPTABLE_OWNER_PID table;
    table = (MIB_TCPTABLE_OWNER_PID*)MALLOC(sizeof(MIB_TCPTABLE_OWNER_PID));
    if(table==NULL)
    {
        std::cout<<"Error Allocating Memory";
        return 0;
    }
    DWORD cbSize = sizeof(MIB_TCPTABLE_OWNER_PID);
    if(GetExtendedTcpTable(table,&cbSize,TRUE,AF_INET,TCP_TABLE_OWNER_PID_ALL,0)==ERROR_INSUFFICIENT_BUFFER)
    {
        FREE(table);
        table = (MIB_TCPTABLE_OWNER_PID*)MALLOC(cbSize);
        if(table==NULL)
        {
            std::cout<<"Error Allocating Memory";
            return 0;
        }
    }
    if(GetExtendedTcpTable(table,&cbSize,TRUE,AF_INET,TCP_TABLE_OWNER_PID_ALL,0)==NO_ERROR)
    {
        struct in_addr IpAddr;
        char szLocalAddr[128];
        char szRemoteAddr[128];
        printf("Number of entries: %d\n", (int) table->dwNumEntries);
        for (int i = 0; i < table->dwNumEntries; i++)
        {
            IpAddr.S_un.S_addr = (u_long) table->table[i].dwLocalAddr;
            strcpy_s(szLocalAddr, sizeof (szLocalAddr), inet_ntoa(IpAddr));
            IpAddr.S_un.S_addr = (u_long) table->table[i].dwRemoteAddr;
            strcpy_s(szRemoteAddr, sizeof (szRemoteAddr), inet_ntoa(IpAddr));
            std::cout<<"PID: "<<table->table[i].dwOwningPid<<"\n";
            HANDLE ps = OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION,0,table->table[i].dwOwningPid);
            
            if (ps==NULL)
            {
                if (table->table[i].dwOwningPid == 0)
                {
                    std::cout<<"\tSystem Idle Process\n";
                }else{
                    std::cout<<"\tFailed to Open Process"<<"\n";
                }
            }else{
                CHAR filename[1024];
                DWORD size = 1024;
                HMODULE mod = LoadLibraryEx(NULL,ps,0);
                DWORD hr = QueryFullProcessImageNameA(ps,0,filename,&size);
                if(SUCCEEDED(hr))
                {
                    std::cout<<"\tProcess Name: "<<filename<<"\n";
                }
            }
            std::cout<<"\tLocal Address: "<<szLocalAddr<<"\n";
            std::cout<<"\tRemote Address: "<<szRemoteAddr<<"\n";
            std::cout<<"------------------------------------------------------------\n";
        }
        FREE(table);
        system("pause");
    }
    return 0;    
}
