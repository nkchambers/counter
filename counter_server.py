from flask import Flask, render_template, request, redirect, session

app = Flask (__name__)
app.secret_key='Heyyooo!'


@app.route('/')
def index():
    if 'click_counter' in session:
        print('add_click')
        session['click_counter'] = session['click_counter']+1
    else:
        print ('no_click')
        session ['click_counter'] = 0

    return render_template ('counter_index.html')


@app.route('/destroy_session')
def destroy_app():
    session.clear()
    
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)