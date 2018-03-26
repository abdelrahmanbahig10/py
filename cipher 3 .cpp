#include <iostream>
#include <string>
using namespace std;

/*
 FCI – Programming 1 – 2018 - Assignment 2
 Program Name:   ROT13 Cipher .cpp
 Last Modification Date: 3/3/2018
 Author1 and ID and Group: Abdelrahman Bahig    20170143    G.6
 Author2 and ID and Group: Abdelrahman Mohamed  20170148    G.6
 Teaching Assistant:  Mohamed Atta
 Purpose:  ROT13 Cipher :  It is a simple letter substitution cipher that replaces a letter with the 13th letter after it, in the alphabet
*/
int main()
{
    int Result ;
    while(true) {
        cout << " \n Ahlan ya user ya habibi .\n \n" ;
        cout << " what do like to do today ? \n\n 1- Cipher a message \n 2- Decipher a message\n 3- End\n  " ;
        cin >> Result ;
        if ( Result == 1){
            string message , text ;
            cout<<"Please Enter the message to Cipher ::"<<endl;
            cin.get() ;
            getline(cin,message);
            for (int i = 0 ; i < message.size(); ++i ){
                    if (( (int) message[i]>= 65 && (int) message[i] <= 77 ) || ((int) message[i]>= 97 && (int) message [i] <= 109  )) {
                            text += ( (char)( (int) message[i] + 13 )  );
                     }
                    else if (( (int) message[i]>= 78 && (int) message[i] <= 90 ) || ((int) message[i]>= 110 && (int) message [i] <= 122  )) {
                        text +=  ( (char) ( (int) message[i]-13 ) ) ;
                    }
                    else if ( message[i] ==' ' ){
                        text += ' ' ;
                        continue ;
                    }
                    else {
                        cout <<  "PLease enter only letters !\n " ;
                        break ;
                    }
            }
            cout << text << endl ;
        }
        else if ( Result == 2){
                string message , text ;
                cout << "Please Enter the message to DeCipher ::" << endl;
                cin.get();
                getline(cin,message);
                for (int i =0 ; i < message.size(); ++i ){
                    if (( (int) message[i]>= 65 && (int) message[i] <= 77 ) || ((int) message[i]>= 97 && (int) message [i] <= 109  )) {
                            text += ( (char)( (int) message[i] + 13 )  );
                     }
                    else if (( (int) message[i]>= 78 && (int) message[i] <= 90 ) || ((int) message[i]>= 110 && (int) message [i] <= 122  )) {
                        text +=  ( (char) ( (int) message[i]-13 ) ) ;
                    }
                    else if ( message [i] ==' ' ){
                        text += ' ' ;
                        continue ;
                    }
                    else {
                        cout <<  " Enter only letters , please  " ;
                        break ;
                    }
            }
            cout << text << endl ;
        }
        else {
                cout << " Good Bye " ;
                return 0;
        }
    }

}


