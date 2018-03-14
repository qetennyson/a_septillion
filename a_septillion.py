import time
import random

start_time = time.time()

i = 0

z = 1000000000000000000000000
while (i < z):
    print("//\n"
          " //\n"
          "  //\n"
          "   //\n"
          "    //\n"
          "     //\n"
          "      //\n"
          "       //\n"
          "        //\n"
          "         //\n"
          "---------------------\n"
          "-----------------\n"
          "-------------//-\n"
          "--------------//-\n"
          "---------------//-----\n"
          "                //\n"
          "      *          //\n"
          "                  //\n"
          "        *   *      //\n"
          "                    //\n"
          "))         *        ||\n"
          "  ))(:>             ||\n"
          " ))                 ||\n"
          "))        *         ||\n"
          "))                  ||\n"
          "        *   *       ||\n"
          "                    ||\n"
          "                    ||\n"
          "||||))              ||\n"
          "||||))              ||\n"
          "//////////)         ||\n"
          ")) )) )))           ||\n"
          "                    ||\n"
          "         *          ||\n"
          "                *   ||\n"
          "       *            ||\n"
          "                    ||\n"
          "                *   ||\n"
          "                    ||\n"
          "         *          ||\n"
          "                    ||\n"
          ")))))               ||\n"
          "))  ))              ||\n"
          "  ))        *       ||\n"
          "))))))))            ||\n"
          ")))||>>             ||\n"
          "           *        ||\n"
          "                    ||\n"
          "                   //\n"
          "                  //\n"
          "                 //\n"
          "                //\n"
          "               //\n"
          "-----------------------\n"
          "             //\n"
          "------------//-------\n"
          "--------------------\n"
          "---------------------\n"
          "------------------------\n"
          "        //\n"
          "       //\n"
          "      //\n"
          "     //\n"
          "    //\n"
          "   //\n"
          "  //\n"
          " //\n"
          "//\n"
          "||\n"
          ""

          )
    if i % 1000000 == 0:
        print "We've reached " + str(i) + " iterations. \n "

        print "We have " + str(z - i) + " iterations to go.\n"

        print "I need to rest (not really lol).  After all, I've been running this program for about...\n"

        run_time = (time.time() - start_time)/60
        print str(run_time) + " minute(s).\n"

        print("That's about " + str(run_time/60) + " hours...\n")

        print "Maybe you'd like a programming challenge while we wait?\n"

        print "If you're up for it, go find... http://codingbat.com/prob/p129125\n"

        print "Hope you text fast. :P"
        time.sleep(random.randint(30, 60))
    i += 1

print("One Septillion!")