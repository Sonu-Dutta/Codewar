//  Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

//  Examples
//  replace("Hi!") === "H!!"
//  replace("!Hi! Hi!") === "!H!! H!!"
//  replace("aeiou") === "!!!!!"
//  replace("ABCDE") === "!BCD!"

#include <string>
#include<iostream>
#include <regex>
using namespace std;
string replace(const string &s)
{
  cout<<regex_replace(s, regex("[aeiouAEIOU]"), "!");
}

int main(){
  replace("Sonu hello");
  return 0;
}