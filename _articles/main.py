from itertools import groupby
import re

class mdproc:
    def processmd(self):

        filepath = '/Users/francis/Downloads/venture-capital-research-master 2/entrepreneurship.md'

        with open(filepath) as f:
            lines = f.readlines()


        for line in lines:
            if line == '\n':

                lines.remove(line)


        articles = (list(g) for k, g in groupby(lines, key=lambda x: x != '---\n') if k)
        for article in articles:

            print '-------'


            print(article)

            for item in article:

                print item[0:3]

                if item[0:3] == "## ":
                    title = item.split("## ")[1].split("\n")[0]

                    print title

                    fn = title.split()

                    filename = ""

                    for n in fn:

                        if fn.index(n) < 5:
                            f = re.sub(r'\W+', '', n)
                            if fn.index(n) != len(fn) and fn.index(n) < 4:
                                filename = filename + f.lower() + "-"
                            else:
                                filename = filename + f.lower()
                        else:
                            pass

                    # fna = re.sub(r'\W+', '', fn)

                    filename = filename + ".md"
                    print filename
                    articlefile = open(filename, "w")

                    articlefile.write("---\n")
                    articlefile.write("layout: article\n")
                    articlefile.write("comments: true\n")

                    articlefile.write("title: " + title + "\n")



                else:
                    if item == "### Summary\n":

                        summaryindex =  article.index(item)

                        # print article[summaryindex + 1]

                        summary = article[summaryindex + 1].rstrip('\n')

                        print summary

                        articlefile.write("excerpt: " + summary + "\n")

                    else:
                        if item[0:15] == '#### [Download]':
                            downloadlink = item.split("[Download](")[1].split("){:target=\"_blank\"}")[0]

                            print downloadlink

                            articlefile.write("link: " + downloadlink + "\n")

                        else:
                            if item[0:9] == "<details>":
                                sourceindex = article.index(item)
                                source = article[sourceindex + 1].rstrip('\n')

                                # print source

                                s = source[4:]

                                # print s
                                #
                                if s[0:1] == '[':

                                    sourcelink = s.split("](")[1].split("){:target=\"_blank\"}")[0]
                                #
                                    print sourcelink

                                    sourcetext = s.split("[")[1].split("]")[0]

                                    print sourcetext

                                    articlefile.write("source: " + sourcetext + "\n")
                                    articlefile.write("sourcelink: " + sourcelink + "\n")
                                #
                                else:
                                    print s

                                    articlefile.write("source: " + s + "\n")



                            else:
                                if item == '### Abstract\n':
                                    abstractindex = article.index(item)
                                    abstract = article[abstractindex + 1].rstrip('\n')

                                    print abstract[2:]

                                    articlefile.write("abstract: " + abstract[2:] + "\n")

                                else:
                                    if item == "### Authors\n":

                                        articlefile.write("authors:\n")

                                        for a in range (1, 5):

                                            authorindex = article.index(item)
                                            author = article[authorindex + a].rstrip('\n')

                                            if author[0:2] == "* ":
                                                authorname = author.split(" - ")[0][2:]
                                                authorinst = author.split(" - ")[1]
                                                print authorname
                                                print authorinst

                                                articlefile.write("  - name: " + authorname + "\n")
                                                articlefile.write("    affiliation: " + authorinst + "\n")
                                            else:
                                                pass

            articlefile.write("---")

            articlefile.close()




mdproc().processmd()
