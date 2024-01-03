#!/usr/bin/env ruby

if ARGV[0]
  result = ARGV[0].scan(/School/).join
  puts result
else
  puts "No input string provided."
end
