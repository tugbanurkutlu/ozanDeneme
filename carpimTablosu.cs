﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CarpimTablosu
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 10 ; i++)
            {
                Console.WriteLine( i + "'in katlari:");
                for ( int j = 1; j <= 10; j++)
                {
                    Console.WriteLine(i+"x"+j,"="+(i * j));
                }
            }
            Console.ReadLine();

        }
    }
}
