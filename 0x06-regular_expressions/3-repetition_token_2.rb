#!/usr/bin/env ruby
# match hbtn, hbtttn, hbttttn, hbtttttn

puts ARGV[0].scan(/hbt+n/).join
