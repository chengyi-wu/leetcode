using System;
using System.Collections.Generic;

public class PriorityQueue<T> where T : IComparable<T>
{
    private IList<T> data;
    private Comparison<T> comparison;
    private int Parent(int i)
    {
        return (i - 1) / 2;
    }
    private int Left(int i)
    {
        return 2 * i + 1;
    }
    private int Right(int i)
    {
        return Left(i) + 1;
    }
    private void Swap(int i, int j)
    {
        var temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }
    private bool LessThan(T a, T b)
    {
        return comparison(a, b) < 0;
    }
    /// <summary>
    /// flow-down
    /// </summary>
    private void Heapify(int i)
    {
        int l = Left(i), r = Right(i);
        var min = i;
        if (l < Count && LessThan(data[l], data[i]))
        {
            min = l;
        }
        if (r < Count && LessThan(data[r], data[min]))
        {
            min = r;
        }
        if (min != i)
        {
            Swap(min, i);
            Heapify(min);
        }
    }

    public PriorityQueue() : this(new List<T>(), (x, y) => x.CompareTo(y))
    {
    }
    public PriorityQueue(Comparison<T> comparison) : this(new List<T>(), comparison) { }
    public PriorityQueue(IList<T> data) : this(data, (x, y) => x.CompareTo(y))
    {
    }
    public PriorityQueue(IList<T> data, Comparison<T> comparison)
    {
        this.data = data;
        this.comparison = comparison;
        
    }
    public void Heapify()
    {
        for (int i = Count / 2 - 1; i >= 0; i--)
        {
            Heapify(i);
        }
    }
    public void Clear()
    {
        data.Clear();
    }
    public int Count
    {
        get { return this.data.Count; }
    }

    public void Push(T item)
    {
        data.Add(item);
        int i = Count - 1;
        while (i > 0 && LessThan(data[i], data[Parent(i)]))
        {
            Swap(i, Parent(i));
            i = Parent(i);
        }
    }

    public T Pop()
    {
        if (Count == 0) return default(T);
        T res = data[0];
        Swap(0, Count - 1);
        data.RemoveAt(Count - 1);
        Heapify(0);
        return res;
    }
    public override string ToString()
    {
        return string.Format("[{0}]", string.Join(", ", data));
    }
}