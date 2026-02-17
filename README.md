# Assignment 3: Record of Tasks — File I/O

This app tracks your IB Computer Science IA project work. The display page already works — run the app and visit `/display` to see pre-loaded tasks. Your job is to build the input form so you can add new tasks.

## Setup

1. Open this project in GitHub Codespaces (or your local environment).
2. Run the app:
   ```
   flask run --debug
   ```
3. Visit `/display` in your browser to confirm you can see the 8 pre-loaded tasks.

## Assignment Requirements

### Step 1: Confirm the display works

Visit `/display` first. You should see a table with 8 sample tasks from Alice, Bob, and Charlie. This page is fully working — study the code in `templates/display.html` and the `/display` route in `app.py` to understand how it reads from the CSV file and renders the data.

### Step 2: Build the HTML form

Open `templates/input.html` and create an HTML form with:

- **student_name** — a text input
- **title** — a text input
- **description** — a textarea
- **criterion** — a select dropdown with options: Planning, Designing, Developing, Testing

Make sure your `<form>` tag includes `method="POST"` and add a submit button.

### Step 3: Complete the POST handler

Open `app.py` and complete the POST handler inside the `/input` route. You need to:

1. Read the form data using `request.form` (e.g., `request.form["title"]`)
2. Generate a datetime stamp using `datetime.now().strftime("%Y-%m-%d %H:%M:%S")`
3. Use `csv.DictWriter` to append a new row to `tasks.csv` (look at how the display route reads the CSV with `csv.DictReader` for clues about the field names)
4. Redirect to the display page using `redirect(url_for("display"))`

### Step 4: Test it

Submit a task through your form, then check that it appears on the display page. Try submitting several tasks and verify they all show up.

### Step 5 (Stretch)

Add client-side validation or additional styling to your form.

## Hints

- The CSV fieldnames are: `datetime`, `student_name`, `title`, `description`, `criterion`
- When opening a file for `csv.DictWriter`, use mode `"a"` (append) and include `newline=""`:
  ```python
  with open("tasks.csv", "a", newline="") as f:
  ```
- Look at the existing display route to see how `csv.DictReader` works — `DictWriter` is the mirror image.
- Each `<input>`, `<textarea>`, and `<select>` in your form **must** have a `name` attribute — that's how Flask knows which field is which.

## What to Submit

Push your completed code to your repository.
