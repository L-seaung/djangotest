#!/usr/bin/env python
# -*- coding:utf-8 -*-

#python version  2.7.12
#system ubuntu 16.04
#auth leeseaung

import scrapy

class stackOvewFlow(scrapy.Spider):
  name = 'stackovewflow'
  start_url = []
  
  def parse(self, response):
    for href in response.css(".question-summary h3 a::attr(href)"):
      full_url = response.urljoin(href.extract())
      yield scrapy.Request(full_url, callback=self.parse_qeustion)
      
  def parse_question(self, response):
  yield{
    'title':response.css('h1 a::text').extract()[0],
    'votes':response.css('.question .vote-count-post::text').extract()[0],
    'body':response.css('.question .post-text').extract()[0],
    'link':response.url,
  }
