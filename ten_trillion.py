import time
import random


start_time = time.time()


def choose_ex(random_assign):
    exercises = {
        'ex_one': "http://codingbat.com/prob/p129125",
        'ex_two': "http://codingbat.com/prob/p135815",
        'ex_three': "http://codingbat.com/prob/p137202",
        'ex_four': "http://codingbat.com/prob/p116620",
        'ex_five': "http://codingbat.com/prob/p119867",
        'ex_six': "http://codingbat.com/prob/p165321",
        'ex_seven': "http://codingbat.com/prob/p195669",
        'ex_eight': "http://codingbat.com/prob/p158497",
        'ex_nine': "http://codingbat.com/prob/p100958"
    }

    if random_assign == 1:
        return exercises['ex_one']
    elif random_assign == 2:
        return exercises['ex_two']
    elif random_assign == 3:
        return exercises['ex_three']
    elif random_assign == 4:
        return exercises['ex_four']
    elif random_assign == 5:
        return exercises['ex_five']
    elif random_assign == 6:
        return exercises['ex_six']
    elif random_assign == 7:
        return exercises['ex_seven']
    elif random_assign == 8:
        return exercises['ex_eight']
    elif random_assign == 9:
        return exercises['ex_nine']


i = 0


END_VALUE = 10000000000000

while i < END_VALUE:
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

        print "We have " + str(END_VALUE - i) + " iterations to go.\n"

        print "I need to rest (not really lol).  After all, I've been running this program for about...\n"

        run_time = (time.time() - start_time)/60
        print '{:02.5f}'.format(run_time) + " minute(s).\n"

        print("That's about " + '{:02.3f}'.format(run_time/60) + " hours...\n")

        print "Maybe you'd like a programming challenge while we wait?\n"

        puzzle = choose_ex(random.randint(1, 5))

        print puzzle

        print "Hope you text fast. :P"
        time.sleep(random.randint(30, 60))

    i += 1

print("Ten Trillion!")