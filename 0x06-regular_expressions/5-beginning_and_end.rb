#!/usr/bin/env ruby
# match any string that starts with 'h' ends with 'n'

puts ARGV[0].scan(/h.n/).join
