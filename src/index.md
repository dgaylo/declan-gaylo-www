{% extends "base.html" %}

{% block canonical_rel %}<link rel="canonical" href="{{ SITEURL }}">{% endblock %}

{% block content %}
<h3>Hello World</h3>
{% endblock %}

{% block banner %}
	{% include 'includes/banner.html' %}
{% endblock %}

