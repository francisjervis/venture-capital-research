---
title: Site Tags
permalink: /tags/

---
<ul>
  {% assign tags = site.data.tags | sort 0 %}
  {% for tag_item in tags %}
  {% assign tag = (tag_item | first) %}
  <li>
    <a href="{{site.url}}{{site.baseurl}}/tags/{{tag}}">{{site.data.tags[tag].name}}</a> (n={{site.data.tags[tag].size}})
  </li>
  {% endfor %}
</ul>
