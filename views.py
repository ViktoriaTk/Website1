from flask import Blueprint, render_template, request, make_response, redirect

views = Blueprint("views", __name__)




@views.route("/")
def page_0():
    return redirect(request.url + "home")


@views.route("/home") 
def home():
    return render_template("/main1.html")


@views.route("/about") 
def about():
    return render_template("/about.html")

@views.route("/portfolio") 
def portfolio():
    return render_template("/portfolio.html")

@views.route("/my_services") 
def my_services():
    return render_template("/my_services.html")

@views.route("/contact_me") 
def contact_me():
    return render_template("/contact_me.html")

@views.route("/idk_somwhere_else_i_guess")
def this_name_can_be_anything_btw():
    return render_template("/somewhere_else.html")
