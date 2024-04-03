#!/usr/bin/env ruby
# match 10 digit numbers, no spaces or any char in the string but just digits

puts ARGV[0].scan(/^[0-9]{10}$/).join
