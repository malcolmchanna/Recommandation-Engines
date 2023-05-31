@app.route('/index' ,methods=['GET', 'POST'] )
def index():
  if 'username' in session:
    search_text = request.form['search_text']
    return redirect('/login')
  else:
    return render_template('/index.html')     

