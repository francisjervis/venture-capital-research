---
title: Site Tags
permalink: /tags/
layout: page
sitemap: false
---
<ul>
  {% assign tags = site.tags | sort 0 %}
  {% for tag_item in tags %}
  {% assign tag = (tag_item | first) %}
  <li>
    <a href="{{site.url}}{{site.baseurl}}/tags/{{tag}}">{{site.data.tags[tag].name}}</a> ({{site.tags[tag].size}})
  </li>
  {% endfor %}
</ul>
