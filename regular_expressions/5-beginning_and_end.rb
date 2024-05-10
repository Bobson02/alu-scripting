#!/usr/bin/env ruby
puts ARGV[0]&.match?(/^h.n$/) ? "Pattern matched: #{ARGV[0]}" : "Pattern not matched: #{ARGV[0]}"

