from svntest.verify import make_diff_header, make_no_diff_deleted_header, \
                           make_diff_header, make_no_diff_deleted_header, \
                           make_git_diff_header, make_diff_prop_header, \
                           make_diff_prop_val, make_diff_prop_deleted, \
                           make_diff_prop_added, make_diff_prop_modified
  svntest.actions.run_and_verify_svn(None,
                                     'svn: E155010: .*foo\' was not found.',
                                     'diff', sbox.ospath('A/D/foo'))
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_reverse_output, [],
  svntest.actions.run_and_verify_svn(expected_reverse_output, [],
  svntest.actions.run_and_verify_svn(expected_rev1_output, [],
  svntest.actions.run_and_verify_svn(expected_rev1_output, [],
                                        expected_status)
                                        check_props=True)
                                        expected_status)
  svntest.actions.run_and_verify_svn(expected_output, [],
                                        expected_status)
    None, [], 'diff', '-r', '1', wc_dir)
    None, [], 'diff', '-r', 'BASE:1', wc_dir)
    None, [], 'diff', '-r', '2:1', wc_dir)
    None, [], 'diff', '-r', '1:2', wc_dir)
    None, [], 'diff', '-r', '1:BASE', wc_dir)
    None, [], 'diff', '-r', '1:2', wc_dir)
    None, [], 'diff', '-r', '1:BASE', wc_dir)
    None, [], 'diff', '-r', '2:1', wc_dir)
    None, [], 'diff', '-r', 'BASE:1', wc_dir)
                                        expected_status)
    None, [], 'diff', '-r', '3:2', wc_dir)
    None, [], 'diff', '-r', 'BASE:2', wc_dir)
                                        expected_status)
                                        expected_status)
  diff_output = svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
    None, [], 'diff', '--old', A_url, '--new', A2_url, rel_path)
    None, [], 'diff', '--old', A_url, '--new', A2_url)
    None, [],
    None, [],
    [], [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
    None, [],
    None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  exit_code, out, err = svntest.actions.run_and_verify_svn(None, [],
  exit_code, out, err = svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  exit_code, out, err = svntest.actions.run_and_verify_svn(None, [],
  exit_code, out, err = svntest.actions.run_and_verify_svn(None, [],
  exit_code, out, err = svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  exit_code, out, err = svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
    None, [], 'diff', '-r', 'prev:head', sbox.wc_dir)
    None, [], 'diff', '-r', 'head:prev', sbox.wc_dir)
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
    None, [], 'diff', '-r', 'prev:head', sbox.wc_dir)
  "show diffs for binary files"
                                        expected_status)
                                        expected_status)
  # Check that we get diff when the first, the second and both files
  # are marked as binary.  First we'll use --force.  Then we'll use
  # the configuration option 'diff-ignore-content-type'.
  for opt in ['--force',
              '--config-option=config:miscellany:diff-ignore-content-type=yes']:
    for range in ['-r1:2', '-r2:1', '-r2:3']:
      exit_code, stdout, stderr = svntest.main.run_svn(None, 'diff', range,
                                                       iota_path, opt)
      for line in stdout:
        if (re_nodisplay.match(line)):
          raise svntest.Failure
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected, [],
  svntest.actions.run_and_verify_svn(expected, [],
  svntest.actions.run_and_verify_svn(expected, [],
  svntest.actions.run_and_verify_svn(expected, [],
  svntest.actions.run_and_verify_svn(expected, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected, [],
  svntest.actions.run_and_verify_svn(expected, [],
                                                "nonexistent") + [
                                                "nonexistent") + [
  expected_output_base_r2 = make_diff_header("foo", "nonexistent",
  expected_output_r1_base = make_diff_header("foo", "nonexistent",
                                                "nonexistent") + [
  expected_output_base_working[3] = "+++ foo\t(nonexistent)\n"
  svntest.actions.run_and_verify_svn([], [],
  svntest.actions.run_and_verify_svn(expected_output_r1_base, [],
  svntest.actions.run_and_verify_svn(expected_output_base_r1, [],
  svntest.actions.run_and_verify_svn(expected_output_r2_working, [],
  svntest.actions.run_and_verify_svn(expected_output_r2_base, [],
  svntest.actions.run_and_verify_svn(expected_output_base_r2, [],
  svntest.actions.run_and_verify_svn(expected_output_base_working, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected_output_r1_wc, [],
  svntest.actions.run_and_verify_svn(expected_output_wc_r1, [],
  svntest.actions.run_and_verify_svn2(None,
  svntest.actions.run_and_verify_svn(expected_output_r1_wc, [],
  svntest.actions.run_and_verify_svn(expected_output_wc_r1, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected_output_r1_wc, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected, [],
  diff_X_r1_base = make_diff_header("X", "nonexistent",
  diff_X_base_r3 = make_diff_header("X", "nonexistent",
  diff_foo_r1_base = make_diff_header("foo", "nonexistent",
  diff_foo_base_r3 = make_diff_header("foo", "nonexistent",
  diff_X_bar_r1_base = make_diff_header("X/bar", "nonexistent",
  diff_X_bar_base_r3 = make_diff_header("X/bar", "nonexistent",
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected_output_r1_base, [],
  svntest.actions.run_and_verify_svn(expected_output_r1_base, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected_output_base_r3, [],
  expected_output_r1_BASE = make_diff_header("X/bar", "nonexistent",
  expected_output_r1_WORKING = make_diff_header("X/bar", "nonexistent",
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected_output_r1_BASE, [],
  svntest.actions.run_and_verify_svn(expected_output_r1_WORKING, [],
  svntest.actions.run_and_verify_svn(None, [],
    svntest.verify.AnyOutput, [], 'diff', '-rBASE:1', newfile)
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(svntest.verify.AnyOutput, [],
  # Get the differences between a deep newly added dir Issue(4421)
  expected_diff = svntest.wc.State(wc_dir, {
    'Q/R'         : Item(status='A '),
    'Q/R/newfile' : Item(status='A '),
    })
  expected_reverse_diff = svntest.wc.State(wc_dir, {
    'Q/R'         : Item(status='D '),
    'Q/R/newfile' : Item(status='D '),
    })
  svntest.actions.run_and_verify_diff_summarize(expected_diff,
                                                p('Q/R'), '-c3')
  svntest.actions.run_and_verify_diff_summarize(expected_reverse_diff,
                                                p('Q/R'), '-c-3')

                                        expected_status)
  svntest.actions.run_and_verify_svn(["J. Random <jrandom@example.com>\n"],
  svntest.actions.run_and_verify_svn(expected_output, [],
                                        None,)
  svntest.actions.run_and_verify_svn([], [],
  svntest.actions.run_and_verify_svn(expected_output, [],
                                        None)
  svntest.actions.run_and_verify_svn(expected_output, [],
                                        None)
                                          None)
  svntest.actions.run_and_verify_svn(expected_output, [],
    svntest.actions.run_and_verify_svn(expected_diffs[depth], [],
  svntest.actions.run_and_verify_svn(None, [],
    svntest.actions.run_and_verify_svn(expected_diffs[depth], [],
  svntest.actions.run_and_verify_svn(None, [],
    svntest.actions.run_and_verify_svn(expected_diffs[depth], [],
                                        None)
  svntest.actions.run_and_verify_svn([], [],
  diff_repos_wc = make_diff_header("A/mucopy", "revision 2", "nonexistent")
  svntest.actions.run_and_verify_svn(diff_repos_wc, [],
                                        expected_status)
    None, ".*--xml' option only valid with '--summarize' option",
  svntest.actions.run_and_verify_svn([], err.INVALID_DIFF_OPTION,
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(None, [],
                         "revision 1", "working copy",
                                         "nonexistent",
  ] + make_git_diff_header(new_path, "new", "nonexistent",
  svntest.actions.run_and_verify_svn(expected, [], 'diff',
                                         "revision 1", "nonexistent",
                           "revision 1", "nonexistent",
                           "revision 1", "nonexistent",
  svntest.actions.run_and_verify_svn(expected, [], 'diff',
  expected_output = make_git_diff_header(new_path, "new", "nonexistent",
  ] + make_git_diff_header(mu_path, "A/mu", "revision 1", "nonexistent",
  svntest.actions.run_and_verify_svn(expected, [], 'diff',
                                         "nonexistent",
    ] + make_git_diff_header("new", "new", "nonexistent", "revision 2",
  svntest.actions.run_and_verify_svn(expected, [], 'diff',
                                        expected_status)
  svntest.actions.run_and_verify_svn(expected_output, [],
                                        expected_status)
  svntest.actions.run_and_verify_svn(expected_output, [],
                                        expected_status)
  expected_output = make_git_diff_header(new_path, "new", "nonexistent",
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff',
                                        expected_status)
                                         "nonexistent", "working copy",
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff',
                                        expected_status)
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff',
  # The same again, but specifying the target explicitly. This should
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff',
                                        expected_status)
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff',
  svntest.actions.run_and_verify_svn(None, [], 'diff', B_abs_path)
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  expected_output = make_diff_header('newdir/newfile', 'nonexistent',
                                         'nonexistent',
                    ] + make_diff_header('A/B/F', 'nonexistent',
                        make_diff_prop_added("newprop",
                                         'nonexistent',
                    ] + make_diff_header('A/D/G/pi', 'nonexistent',
                                         'nonexistent',
                                         'nonexistent',
                                         'nonexistent',
                    ] + make_diff_header('A/B/F', 'working copy',
                                         'nonexistent',
                                         src_label, dst_label) + \
                        make_diff_prop_header('A/B/F') + \
                        make_diff_prop_deleted('newprop', 'propval-old\n')

  # Files in diff may be in any order. #### Not any more, but test order is wrong.
  svntest.actions.run_and_verify_svn(expected_output, [],
  expected_output = make_diff_header("chi", "revision 1", "nonexistent") + [
                                         "nonexistent") + [
                                         "nonexistent") + [
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  expected_output = make_diff_header("G/pi", "nonexistent", "working copy",
                    ] + make_diff_header("G/rho", "nonexistent",
                    ] + make_diff_header("G/tau", "nonexistent",
                    ] + make_diff_header("H/chi", "nonexistent",
                    ] + make_diff_header("H/omega", "nonexistent",
                    ] + make_diff_header("H/psi", "nonexistent",
                                         "nonexistent", "B/E", "D") + [
                                         "nonexistent", "B/E", "D") + [
                    ] + make_diff_header("gamma", "nonexistent",
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_reverse_output, [],
  svntest.actions.run_and_verify_svn(expected_rev1_output, [],
  svntest.actions.run_and_verify_svn(expected_rev1_output, [],
    svntest.actions.run_and_verify_svn(expected_output, [], 'diff')
    svntest.actions.run_and_verify_svn(None, [], 'revert', 'iota')
  svntest.actions.run_and_verify_svn([], [],
  svntest.actions.run_and_verify_svn([], [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
  _, out, _ = svntest.actions.run_and_verify_svn(None, [],
  svntest.actions.run_and_verify_svn(None, [], 'revert', '-R', wc_dir)
  svntest.actions.run_and_verify_svn(expected_output, [],
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/alpha'),
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/beta'),
    '--- %s\t(nonexistent)\n' % sbox.path('A/B/E'),
  svntest.actions.run_and_verify_svn(expected_output, [],
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/alpha'),
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/beta'),
    '--- %s\t(nonexistent)\n' % sbox.path('A/B/E/beta'),
    '--- %s\t(nonexistent)\n' % sbox.path('A/B/E'),
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/alpha'),
  svntest.actions.run_and_verify_svn(expected_output, [],
  svntest.actions.run_and_verify_svn(expected_output, [],
                                        expected_status)
  svntest.actions.run_and_verify_svn(expected_output, [],
                                       [], False, False,
                                       '--ignore-ancestry', wc_dir)
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff', wc_dir)
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff', wc_dir)
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff', wc_dir)
  svntest.actions.run_and_verify_svn(svntest.verify.AnyOutput, [],
  svntest.actions.run_and_verify_svn(svntest.verify.AnyOutput, [],
@XFail()
@Issue(4464)
def diff_repo_wc_copies(sbox):
  "diff repo to wc of a copy"
  sbox.build()
  wc_dir = sbox.wc_dir
  iota_copy = sbox.ospath('iota_copy')
  iota_url = sbox.repo_url + '/iota'

  sbox.simple_copy('iota', 'iota_copy')
  expected_output = make_diff_header(iota_copy, "nonexistent", "working copy",
                                     iota_url, iota_copy) + [
                                       "@@ -0,0 +1 @@\n",
                                       "+This is the file 'iota'.\n" ]
  svntest.actions.run_and_verify_svn(expected_output, [], 'diff',
                                     '--show-copies-as-adds',
                                     iota_url, iota_copy)

@Issue(4460)
def diff_repo_wc_file_props(sbox):
  "diff repo to wc file target with props"
  sbox.build()
  iota = sbox.ospath('iota')

  # add a mime-type and a line to iota to test the binary check
  sbox.simple_propset('svn:mime-type', 'text/plain', 'iota')
  sbox.simple_append('iota','second line\n')

  # test that we get the line and the property add
  expected_output = make_diff_header(iota, 'revision 1', 'working copy') + \
                    [ '@@ -1 +1,2 @@\n',
                      " This is the file 'iota'.\n",
                      "+second line\n", ] + \
                    make_diff_prop_header(iota) + \
                    make_diff_prop_added('svn:mime-type', 'text/plain')
  svntest.actions.run_and_verify_svn(expected_output, [],
                                     'diff', '-r1', iota)

  # reverse the diff, should get a property delete and line delete
  expected_output = make_diff_header(iota, 'working copy', 'revision 1') + \
                    [ '@@ -1,2 +1 @@\n',
                      " This is the file 'iota'.\n",
                      "-second line\n", ] + \
                    make_diff_prop_header(iota) + \
                    make_diff_prop_deleted('svn:mime-type', 'text/plain')
  svntest.actions.run_and_verify_svn(expected_output, [],
                                     'diff', '--old', iota,
                                     '--new', iota + '@1')

  # copy iota to test with --show-copies as adds
  sbox.simple_copy('iota', 'iota_copy')
  iota_copy = sbox.ospath('iota_copy')

  # test that we get all lines as added and the property added
  # TODO: We only test that this test doesn't error out because of Issue #4464
  # if and when that issue is fixed this test should check output
  svntest.actions.run_and_verify_svn(None, [], 'diff',
                                     '--show-copies-as-adds', '-r1', iota_copy)

  # reverse the diff, should get all lines as a delete and no property
  # TODO: We only test that this test doesn't error out because of Issue #4464
  # if and when that issue is fixed this test should check output
  svntest.actions.run_and_verify_svn(None, [], 'diff',
                                     '--show-copies-as-adds',
                                     '--old', iota_copy,
                                     '--new', iota + '@1')

  # revert and commit with the eol-style of LF and then update so
  # that we can see a change on either windows or *nix.
  sbox.simple_revert('iota', 'iota_copy')
  sbox.simple_propset('svn:eol-style', 'LF', 'iota')
  sbox.simple_commit() #r2
  sbox.simple_update()

  # now that we have a LF file on disk switch to CRLF
  sbox.simple_propset('svn:eol-style', 'CRLF', 'iota')

  # test that not only the property but also the file changes
  # i.e. that the line endings substitution works
  if svntest.main.is_os_windows():
    # test suite normalizes crlf output into just lf on Windows.
    # so we have to assume it worked because there is an add and
    # remove line with the same content.  Fortunately, it doesn't
    # do this on *nix so we can be pretty sure that it works right.
    # TODO: Provide a way to handle this better
    crlf = '\n'
  else:
    crlf = '\r\n'
  expected_output = make_diff_header(iota, 'revision 1', 'working copy') + \
                    [ '@@ -1 +1 @@\n',
                      "-This is the file 'iota'.\n",
                      "+This is the file 'iota'." + crlf ] + \
                    make_diff_prop_header(iota) + \
                    make_diff_prop_added('svn:eol-style', 'CRLF')

  svntest.actions.run_and_verify_svn(expected_output, [],
                                     'diff', '-r1', iota)


@Issue(4460)
def diff_repo_repo_added_file_mime_type(sbox):
    "diff repo to repo added file with mime-type"
    sbox.build()
    wc_dir = sbox.wc_dir
    newfile = sbox.ospath('newfile')

    # add a file with a mime-type
    sbox.simple_append('newfile', "This is the file 'newfile'.\n")
    sbox.simple_add('newfile')
    sbox.simple_propset('svn:mime-type', 'text/plain', 'newfile')
    sbox.simple_commit() # r2

    # try to diff across the addition
    expected_output = make_diff_header(newfile, 'nonexistent', 'revision 2') + \
                      [ '@@ -0,0 +1 @@\n',
                        "+This is the file 'newfile'.\n" ] + \
                      make_diff_prop_header(newfile) + \
                      make_diff_prop_added('svn:mime-type', 'text/plain')

    svntest.actions.run_and_verify_svn(expected_output, [], 'diff',
                                       '-r1:2', newfile)

    # reverse the diff to diff across a deletion
    expected_output = make_diff_header(newfile, 'revision 2', 'nonexistent') + \
                      [ '@@ -1 +0,0 @@\n',
                        "-This is the file 'newfile'.\n",
                        '\n',
                        'Property changes on: %s\n' % sbox.path('newfile'),
                        '__________________________________________________' +
                              '_________________\n',
                        'Deleted: svn:mime-type\n',
                        '## -1 +0,0 ##\n',
                        '-text/plain\n',
                        '\ No newline at end of property\n']
    svntest.actions.run_and_verify_svn(expected_output, [], 'diff',
                                       '-r2:1', newfile)

def diff_switched_file(sbox):
  "diff a switched file against repository"

  sbox.build()
  svntest.actions.run_and_verify_svn(None, [], 'switch',
                                     sbox.repo_url + '/A/mu',
                                     sbox.ospath('iota'), '--ignore-ancestry')
  sbox.simple_append('iota', 'Mu????')

  # This diffs the file against its origin
  expected_output = [
    'Index: %s\n' % sbox.path('iota'),
    '===================================================================\n',
    '--- %s\t(.../A/mu)\t(revision 1)\n' % sbox.path('iota'),
    '+++ %s\t(.../iota)\t(working copy)\n' % sbox.path('iota'),
    '@@ -1 +1,2 @@\n',
    ' This is the file \'mu\'.\n',
    '+Mu????\n',
    '\ No newline at end of file\n',
  ]
  svntest.actions.run_and_verify_svn(expected_output, [],
                                     'diff', '-r', '1', sbox.ospath('iota'))

  # And this undoes the switch for the diff
  expected_output = [
    'Index: %s\n' % sbox.path('iota'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('iota'),
    '+++ %s\t(working copy)\n' % sbox.path('iota'),
    '@@ -1 +1,2 @@\n',
    '-This is the file \'iota\'.\n',
    '+This is the file \'mu\'.\n',
    '+Mu????\n',
    '\ No newline at end of file\n',
  ]
  svntest.actions.run_and_verify_svn(expected_output, [],
                                     'diff', '-r', '1', sbox.ospath(''))

def diff_parent_dir(sbox):
  "diff parent directory"

  sbox.build()
  wc_dir = sbox.wc_dir

  svntest.actions.run_and_verify_svnmucc(None, [],
                                         '-U', sbox.repo_url, '-m', 'Q',
                                         'mkdir', 'A/ZZZ',
                                         'propset', 'A', 'B', 'A/ZZZ')

  was_cwd = os.getcwd()
  os.chdir(os.path.join(wc_dir, 'A', 'B'))
  try:
    # This currently (1.8.9, 1.9.0 development) triggers an assertion failure
    # as a non canonical relpath ".." is used as diff target

    expected_output = [
      'Index: ../ZZZ\n',
      '===================================================================\n',
      '--- ../ZZZ	(revision 2)\n',
      '+++ ../ZZZ	(nonexistent)\n',
      '\n',
      'Property changes on: ../ZZZ\n',
      '___________________________________________________________________\n',
      'Deleted: A\n',
      '## -1 +0,0 ##\n',
      '-B\n',
      '\ No newline at end of property\n',
    ]

    svntest.actions.run_and_verify_svn(expected_output, [],
                                     'diff', '-r', '2', '..')

    expected_output = [
      'Index: ../../A/ZZZ\n',
      '===================================================================\n',
      '--- ../../A/ZZZ	(revision 2)\n',
      '+++ ../../A/ZZZ	(nonexistent)\n',
      '\n',
      'Property changes on: ../../A/ZZZ\n',
      '___________________________________________________________________\n',
      'Deleted: A\n',
      '## -1 +0,0 ##\n',
      '-B\n',
      '\ No newline at end of property\n',
    ]

    svntest.actions.run_and_verify_svn(expected_output, [],
                                     'diff', '-r', '2', '../..')
  finally:
    os.chdir(was_cwd)

def diff_deleted_in_move_against_repos(sbox):
  "diff deleted in move against repository"

  sbox.build()
  sbox.simple_move('A/B', 'BB')
  sbox.simple_move('BB/E/alpha', 'BB/q')
  sbox.simple_rm('BB/E/beta')

  svntest.actions.run_and_verify_svn(None, [],
                                     'mkdir', sbox.repo_url + '/BB/E',
                                     '--parents', '-m', 'Create dir')

  # OK. Local diff
  svntest.actions.run_and_verify_svn(None, [],
                                     'diff', sbox.wc_dir)

  # OK. Walks nodes locally from wc-root, notices ancestry
  svntest.actions.run_and_verify_svn(None, [],
                                     'diff', sbox.wc_dir, '-r1',
                                     '--notice-ancestry')

  # OK. Walks nodes locally from BB, notices ancestry
  svntest.actions.run_and_verify_svn(None, [],
                                     'diff', sbox.wc_dir, '-r2',
                                     '--notice-ancestry')

  # OK. Walks nodes locally from wc-root
  svntest.actions.run_and_verify_svn(None, [],
                                     'diff', sbox.wc_dir, '-r1')

  # Assertion. Walks nodes locally from BB.
  svntest.actions.run_and_verify_svn(None, [],
                                     'diff', sbox.wc_dir, '-r2')

def diff_replaced_moved(sbox):
  "diff against a replaced moved node"

  sbox.build(read_only=True)
  sbox.simple_move('A', 'AA')
  sbox.simple_rm('AA/B')
  sbox.simple_move('AA/D', 'AA/B')

  # Ok
  svntest.actions.run_and_verify_svn(None, [],
                                     'diff', sbox.ospath('.'), '-r1')

  # Ok (rhuijben: Works through a hack assuming some BASE knowledge)
  svntest.actions.run_and_verify_svn(None, [],
                                     'diff', sbox.ospath('AA'), '-r1')

  # Error (misses BASE node because the diff editor is driven incorrectly)
  svntest.actions.run_and_verify_svn(None, [],
                                     'diff', sbox.ospath('AA/B'), '-r1')

# Regression test for the fix in r1619380. Prior to this (and in releases
# 1.8.0 through 1.8.10) a local diff incorrectly showed a copied dir's
# properties as added, whereas it should show only the changes against the
# copy-source.
def diff_local_copied_dir(sbox):
  "local WC diff of copied dir"

  sbox.build()

  was_cwd = os.getcwd()
  os.chdir(sbox.wc_dir)
  sbox.wc_dir = ''

  try:
    sbox.simple_propset('p1', 'v1', 'A/C')
    sbox.simple_commit()

    # dir with no prop changes
    sbox.simple_copy('A/C', 'C2')
    # dir with prop changes
    sbox.simple_copy('A/C', 'C3')
    sbox.simple_propset('p2', 'v2', 'C3')

    expected_output_C2 = []
    expected_output_C3 = [
      'Index: C3\n',
      '===================================================================\n',
      '--- C3	(revision 2)\n',
      '+++ C3	(working copy)\n',
      '\n',
      'Property changes on: C3\n',
      '___________________________________________________________________\n',
      'Added: p2\n',
      '## -0,0 +1 ##\n',
      '+v2\n',
      '\ No newline at end of property\n',
    ]

    svntest.actions.run_and_verify_svn(expected_output_C2, [],
                                       'diff', 'C2')
    svntest.actions.run_and_verify_svn(expected_output_C3, [],
                                       'diff', 'C3')
  finally:
    os.chdir(was_cwd)

              diff_repo_wc_copies,
              diff_repo_wc_file_props,
              diff_repo_repo_added_file_mime_type,
              diff_switched_file,
              diff_parent_dir,
              diff_deleted_in_move_against_repos,
              diff_replaced_moved,
              diff_local_copied_dir,