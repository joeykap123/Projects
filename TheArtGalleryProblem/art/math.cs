using System;
using static System.Math;

public class Polygon
{
    public int numOfSides;

    public static void Main(string[] args)
    {
        Console.WriteLine("Enter the number of sides your simple polygon has: ");
        String userInput = Console.ReadLine();
        int number;
        if (int.TryParse(userInput, out number))
        {
            Polygon x = new Polygon(number);
            Console.WriteLine(x.toString());
        }
        else
        {
            String message = "Solution requires an integer type value, as polygons cannot have fractional side amounts";
            Console.WriteLine($"Error: Ensure input is an integer Details: {message}");
        }
    }
    
    /// <summary>
    /// Constructor for polygon class
    /// </summary>
    /// <param name="numberOfSides">An int representing the number of sides the given polygon has</param>
    public Polygon(int numberOfSides)
    {
        if (numberOfSides <= 0)
        {
            String message = "Solution failed. Please ensure the number of sides is larger than 0.";
            Console.WriteLine($"Error: Cannot execute program. Details {message}");
        }
        this.numOfSides = numberOfSides;
    }

    /// <summary>
    /// Computes tight upper limit of guards required to survey gallery. Uses Chvátal's method.
    /// </summary>
    /// <returns>An int representing the maximum amount of guards that would ever be needed. </returns>
    public int naiveSolution()
    {
        return this.numOfSides / 3;
    }

    /// <summary>
    /// toString implementation
    /// </summary>
    /// <returns>A string detailing the number of sides the polygon has and how many guards are needed.</returns>
    public String toString()
    {
        return $"Polygon given has {this.numOfSides} sides and requires at most {this.naiveSolution()} guards.";
    }

}

