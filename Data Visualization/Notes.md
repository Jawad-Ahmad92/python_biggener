# Matplotlib Notes

## What is Matplotlib?

**Definition:**
Matplotlib is a Python library used to create graphs and charts from data.

### Why do we use Matplotlib?

- To show data visually.
- To compare values.
- To understand data easily.
- To find patterns and trends.

### Import Matplotlib

````python
import matplotlib.pyplot as plt


`pyplot` is the part of Matplotlib used to draw graphs.



# Basic Plot Structure

```python
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [2,4,6,8]

plt.plot(x,y)
plt.show()
````

### Explanation

- `x` = Horizontal values
- `y` = Vertical values
- `plot()` = Draw graph
- `show()` = Display graph

# 1. Line Graph

## Definition

A line graph joins points with lines.

### Used for

- Showing trends
- Growth over time
- Temperature
- Sales

```python
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,15,30]

plt.plot(x,y)
plt.show()
```

### Important Functions

```python
plt.title("Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
```

# Change Line Color

```python
plt.plot(x,y,color="red")
```

<!--  -->

# Change Line Style

```python
plt.plot(x,y,linestyle="--")
```

Styles

- "-"
- "--"
- "-."
- ":"

# Change Line Width

```python
plt.plot(x,y,linewidth=3)
```

# Add Marker

```python
plt.plot(x,y,marker="o")
```

Markers

- o
- -
- x
- s
- ^
- -

# Grid

```python
plt.grid()
```

# Legend

```python
plt.plot(x,y,label="Sales")
plt.legend()
```

# Figure Size

```python
plt.figure(figsize=(8,5))
```

# 2. Scatter Plot

## Definition

Scatter plot shows individual data points.

### Used for

- Compare two values
- Find relationship
- Machine Learning

```python
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[5,8,6,9]

plt.scatter(x,y)
plt.show()
```

### Change Color

```python
plt.scatter(x,y,color="green")
```

### Change Size

```python
plt.scatter(x,y,s=100)
```

# 3. Bar Chart

## Definition

Bar chart compares different categories.

### Used for

- Student marks
- Product sales
- Population

```python
name=["Ali","Ahmed","Sara"]
marks=[80,70,90]

plt.bar(name,marks)
plt.show()
```

### Horizontal Bar Chart

```python
plt.barh(name,marks)
```

### Change Color

```python
plt.bar(name,marks,color="orange")
```

# 4. Histogram

## Definition

Histogram shows frequency of data.

### Used for

- Age
- Marks
- Salary

```python
data=[10,20,20,30,30,30,40]

plt.hist(data)
plt.show()
```

### Number of Bins

```python
plt.hist(data,bins=5)
```

# 5. Pie Chart

## Definition

Pie chart shows percentages.

### Used for

- Budget
- Expenses
- Market share

```python
labels=["A","B","C"]
sizes=[30,40,30]

plt.pie(sizes,labels=labels)
plt.show()
```

### Show Percentage

```python
plt.pie(sizes,labels=labels,autopct="%1.1f%%")
```

# 6. Box Plot

## Definition

Box plot shows data spread and outliers.

### Used for

- Data analysis
- Statistics
- Finding unusual values

```python
data=[10,20,30,40,50]

plt.boxplot(data)
plt.show()
```

# 7. Area Chart

## Definition

Area chart is like a line graph with color filled below it.

```python
x=[1,2,3,4]
y=[2,4,6,8]

plt.fill_between(x,y)
plt.show()
```

# 8. Stack Plot

## Definition

Stack plot shows multiple datasets together.

```python
x=[1,2,3,4]
y1=[2,3,4,5]
y2=[1,2,3,2]

plt.stackplot(x,y1,y2)
plt.show()
```

# 9. Stem Plot

## Definition

Shows values using vertical lines.

```python
x=[1,2,3,4]
y=[10,15,8,20]

plt.stem(x,y)
plt.show()
```

# 10. Step Plot

## Definition

Shows data in step form.

```python
plt.step(x,y)
plt.show()
```

# 11. Error Bar Plot

## Definition

Shows data with error values.

```python
x=[1,2,3]
y=[10,20,30]
error=[1,2,1]

plt.errorbar(x,y,yerr=error)
plt.show()
```

# 12. Multiple Graphs

```python
plt.plot(x,y,label="Line")

plt.scatter(x,y,label="Points")

plt.legend()

plt.show()
```

# Subplots

## Definition

Subplots display multiple graphs in one figure.

```python
plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.bar(x,y)

plt.show()
```

# Save Graph

```python
plt.savefig("graph.png")
```

# Close Graph

```python
plt.close()
```

# Clear Graph

```python
plt.clf()
```

# Common Colors

```python
red
blue
green
yellow
black
orange
purple
pink
```

# Common Markers

```python
o
*
x
+
s
^
D
```

# Common Line Styles

```python
-
--
-.
:
```

# Most Important Functions

| Function             | Purpose              |
| -------------------- | -------------------- |
| `plt.plot()`         | Line graph           |
| `plt.scatter()`      | Scatter plot         |
| `plt.bar()`          | Vertical bar chart   |
| `plt.barh()`         | Horizontal bar chart |
| `plt.hist()`         | Histogram            |
| `plt.pie()`          | Pie chart            |
| `plt.boxplot()`      | Box plot             |
| `plt.fill_between()` | Area chart           |
| `plt.stackplot()`    | Stack plot           |
| `plt.step()`         | Step plot            |
| `plt.stem()`         | Stem plot            |
| `plt.errorbar()`     | Error bar graph      |
| `plt.title()`        | Add title            |
| `plt.xlabel()`       | X-axis label         |
| `plt.ylabel()`       | Y-axis label         |
| `plt.legend()`       | Show legend          |
| `plt.grid()`         | Show grid            |
| `plt.figure()`       | Set figure size      |
| `plt.subplot()`      | Multiple graphs      |
| `plt.savefig()`      | Save graph           |
| `plt.show()`         | Display graph        |

# Short Exam Definition

**Matplotlib:**
Matplotlib is a Python library used to create graphs and charts for data visualization. It helps us understand data by displaying it in visual form.

# Important Exam Points

- Matplotlib is used for **data visualization**.
- Import using `import matplotlib.pyplot as plt`.
- Always use `plt.show()` to display the graph.
- Use `plt.title()`, `plt.xlabel()`, and `plt.ylabel()` to make graphs easy to understand.
- The most important graphs are:
  - Line Plot
  - Scatter Plot
  - Bar Chart
  - Histogram
  - Pie Chart
  - Box Plot
  - Area Chart
  - Stack Plot

  - Step Plot
  - Stem Plot
  - Error Bar Plot
  - Subplots

These notes cover the main Matplotlib topics that are commonly taught in beginner Python, data analysis, and machine learning courses.
